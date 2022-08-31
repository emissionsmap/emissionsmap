import pandas as pd
from googletrans import Translator
from select import select
import psycopg2
from fuzzywuzzy import fuzz, process
import hashlib

from pathlib import Path
import os



#Funcion que recibe como parametro una DF para evaluacion de la calidad de los datos de este
def calidaDato (data):
    df = data
    calidad = []
    mascara = df.isna().sum() #mascara con la suma d los datos nulos
    for i in range(0,len(mascara)):
        p = (df.shape[0]- mascara[i]) / df.shape[0] #colum[(total - nulo)/total]
        calidad.append([mascara.index[i], round((p*100),2)]) #Agregando el % d ecalidad
   
    calidad = pd.DataFrame(calidad)
    calidad.rename(columns={0:'Columna', 1: 'Calida %'}, inplace=True)
    
    return calidad

#funcion para subir un archivo a una carpeta en especifico
def subircsv(nomcarpeta, nomarchivo, extencion, df): #parametros de nomb de carpeta a guadar, nombre del archivo, la extencion(csv) y el dataframe.
    df = df
    filepath = Path(nomcarpeta + '/' + nomarchivo +'.' + extencion)  
    filepath.parent.mkdir(parents=True, exist_ok=True)  #
    df.to_csv(filepath) 
    return print('Archivo cargado exitosamente')

#funcion para renombrar columas de ingles a español
def renombracol(data):
    data = data
    translator = Translator() #metodo de google
    for i in data.columns:
        b = i.replace('_',' ') #Iteracion para cambiar caracter
        data.rename(columns={i:b}, inplace=True) 
        data.rename(columns={'owner':'owne'}, inplace=True)
        
    for i in data.columns:
        data.rename(columns={i:translator.translate(i, dest="es").text.title()}, inplace=True) #iterecion para obtenr nombre de columna y traducir
        
    return data

#Funicon para crear un ID unico 
def crearhash(DataFrame):
    for i in DataFrame.columns:
        if i == "País" or i == "Combustible" or i == "Año" or  i == "Continente": #ombre de las tablas especificos que nesecitamos ID
            nom = "Id_" + i
            if DataFrame[i].dtype == 'int64':
                DataFrame[i] = DataFrame[i].astype(str)
                DataFrame[nom] = DataFrame[i].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
                DataFrame[i] = DataFrame[i].astype(int)
            else:
                nom = "Id_" + i
                DataFrame[nom] = DataFrame[i].apply(lambda x: hashlib.md5(x.encode()).hexdigest())
    return DataFrame


#Normalizar nombre de los campos para obtener metricas correctas
def fuzz(df, colum):
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


#Funicon para la obtendion de los indicadores de quantiles
def quan(df, nomId, nomQua): #se le pasa dataframe, nombre (ID) y el campo a analizar
    lista_id = []
    lista_minimo= []
    lista_maximo= []
    uni = df[nomId].unique()  
    i_max = len(df[nomId].unique())
    i = 0 
     
    for id in uni:
        i+=1    
        q1 = df[df[nomId] == id][nomQua].quantile(0.25) # Cuantil < 25%
        mediana = df[df[nomId] == id][nomQua].quantile(0.5) #Media
        q3 = df[df[nomId] == id][nomQua].quantile(0.75) # cuantil > 75%
        
        iqr = q3 - q1 #rango intercuartil
        minimo = mediana - 1.5 * iqr # < 15%
        maximo = mediana + 1.5 * iqr # > 75%  
        if (minimo< 0.001):
            minimo= 0.001
            
        lista_id.append(id)
        lista_minimo.append(minimo)
        lista_maximo.append(maximo)
        
        lst = list(zip(lista_id, lista_minimo, lista_maximo))
        dfin = pd.DataFrame(lst , columns = [nomId,'minimo','maximo'])   
        
    
        clear_output(wait=True)
        print('Completado: ' + str(round(i / i_max * 100, 2)) + '%')
    
    return dfin




