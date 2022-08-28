import pandas as pd
import numpy as np
import hashlib
import csv
import os
from googletrans import Translator
from fuzzywuzzy import fuzz, process

#Encuentra el delimitador de un archivo
def _delimitador (path):
    if path[-4:] == ".txt":
        delimiter = ","
    else:
        data = open(path, "r", encoding="latin_1").read()
        delimiter = csv.Sniffer().sniff(data).delimiter
    return delimiter  

#Encuentra archivos de directorio y sub directorio 
def _archivos(path):
    archivos = []
    rutas = []
    with os.scandir(path) as ficheros:
        for i in ficheros:
            directorio, extencion = os.path.splitext(i)
            if extencion == "":
                rutas, archivos = _archivos(directorio)
                return rutas, archivos     
            else:
                ruta = directorio + extencion
                arch = os.path.basename(ruta)
                archivos.append(arch)
                rutas.append(ruta)    

        return rutas, archivos

        
def _traducirColumnas (df):
    translator = Translator()
    for i in df.columns:
        if i == "Entity":
            df.rename(columns={i:"País"}, inplace=True)
        else:
            df.rename(columns={i:translator.translate(i, dest="es").text.title()}, inplace=True)
    return df


def _crearhash(DataFrame):
    for i in DataFrame.columns:
        if i == "País" or i == "Combustible" or i == "Año" or  i == "Continente":
            nom = "Id_" + i
            if DataFrame[i].dtype == 'int64':
                DataFrame[i] = DataFrame[i].astype(str)
                DataFrame[nom] = DataFrame[i].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
                DataFrame[i] = DataFrame[i].astype(int)
            else:
                nom = "Id_" + i
                DataFrame[nom] = DataFrame[i].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
    return DataFrame


def _fuzz(df, colum):
    correcto = ['Biomass',
                'Coal',
                'Cogeneration',
                'Gas',
                'Geothermal',
                'Hydro',
                'Nuclear',
                'Oil',
                'Other',
                'Petcoke',
                'Solar',
                'Storage',
                'Waste',
                'Wave and Tidal',
                'Wind',
                'all energy types',
                'natural gas',
                'petroleum and other liquids',
                'nuclear',
                'renewables and other']
    df[colum] = df[colum].apply(lambda x: process.extractOne(x,correcto)[0])
    return df

def _limpieza_energy (df):

    df = _traducirColumnas(df)
    df.drop(columns="Sin Nombre: 0", inplace=True)


    otro = pd.read_csv("/home/dio-pc/Escritorio/Lab-grup/archivosPrueba/owid-energy-consumption-source.csv", delimiter=",", encoding="utf-8")
    otro = otro[["year","country","population","gdp"]]
    df = pd.merge(df, otro, left_on=["Año","País"], right_on=["year","country"], how="left")
    df.loc[(df["Población"].isna() == True) & (df["population"].isna() == False), "Población"] = df.loc[(df["Población"].isna() == True) & (df["population"].isna() == False)]["population"]
    df.loc[(df["Pib"].isna() == True) & (df["gdp"].isna() == False), "Pib"] = df.loc[(df["Pib"].isna() == True) & (df["gdp"].isna() == False)]["gdp"]
    df.drop(columns=["country", "year", "population","gdp"], inplace=True)

    df.dropna(subset=["Emisión De Co2"], inplace=True)

    for i in df.columns:
        if i == "Tipo_Energia":
            df.rename(columns={i:"Combustible"}, inplace=True)
        elif "Energ" in i:
            nom = i + " " + "TWh"
            df[nom] = df[i] / 3.412e+12

    df = _fuzz(df, "Combustible")
    df = _crearhash(df)
    return df


def _limpieza_general (df):
    for i in df.columns:
        if "Entity" in i or "Country_long" in i:
            df.rename(columns={i:"País"})
        else:
            continue
    df = _traducirColumnas(df)
    df = _crearhash(df)

    return df

def dataFrame (root):
    rutas, archivos = _archivos(root)
    os.mkdir("Normalizados")
    n = 0
    for i in rutas:
        for e in archivos:
            if e in i:
                if e == "energyco2.csv":
                    deli = _delimitador(i)
                    nombre = "Normal_" + e 
                    df = pd.read_csv(i, low_memory=False)
                    df = _limpieza_energy(df)
                    salida = "./Normalizados/" + nombre
                    df.to_csv(salida, index=False)
                    n+=1
                    print("{} Archivo subido".format(n))
                                      
                else:
                    deli = _delimitador(i)
                    nombre = "Normal_" + e 
                    df = pd.read_csv(i, low_memory=False, on_bad_lines="skip")
                    df = _limpieza_general(df)
                    salida = "./Normalizados/" + nombre
                    df.to_csv(salida, index=False)
                    n+=1
                    print("{} Archivo subido".format(n))
        

        
if __name__ == "__main__":
    try:
        directorio = os.getcwd()
        dataFrame(directorio)
        print("¡¡Archivos normalizados!!")
    except Exception as ex:
        print(ex)