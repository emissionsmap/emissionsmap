from sqlalchemy import create_engine
from configparser import ConfigParser
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
file = (os.path.join(BASE_DIR.parent,'config.ini'),)
config = ConfigParser()
config.read(file)

def db_connection(user,passw,db,port,host):    
    create_connection = f'postgresql+psycopg2://{user}:{passw}@{host}:{port}/{db}'
    connection = create_engine(create_connection)
    return connection

def get_connection():
    return db_connection(config['database']['user'],
                        config['database']['passw'],
                        config['database']['db'],
                        config['database']['port'],
                        config['database']['host'])

def read_db_table(name:str):
    import pandas as pd
    df = pd.read_sql(sql=name,con =get_connection())
    return df