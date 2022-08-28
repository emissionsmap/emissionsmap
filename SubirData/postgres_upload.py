import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
import os
import pandas as pd

def baseDeDatos (df, tabla):
    try:
        conex = create_engine("postgresql+psycopg2://root:UH39qeH&MN^J5!@database-2.ct7rxsgbwels.sa-east-1.rds.amazonaws.com/Laboratorio")
        conexpostgres = conex.connect()
        metadatas = sqlalchemy.MetaData()
        df.to_sql(tabla, conexpostgres, if_exists="append", index=False)
        return "Tabla subida"
    except Exception as ex:
        return ex

with os.scandir("./Normalizados") as ficheros:
    for i in ficheros:
        dir= "./Normalizados/" + i.name
        df = pd.read_csv(dir)
        if i.name == "Tabla_Hecho":
            baseDeDatos(df, i.name)
        else:
            tabla = i.name[7:-4]
            baseDeDatos(df, tabla)