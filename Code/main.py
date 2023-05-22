import pandas as pd
import numpy as np
from dotenv import load_dotenv
import pymysql
import sqlalchemy as alch
from getpass import getpass
from geopy.geocoders import Nominatim 
import os


def ufo_table_from_sql(query):
    load_dotenv()
    password = os.getenv('password')
    dbName = 'UFO'
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    df = pd.read_sql_query(query, engine)
    df = df.sort_values(by='year', axis=0)
    df = df.reset_index()
    del df['index']
    df = df.reindex(columns=['latitude', 'longitude', 'year', 'Cow incidents', 'Crop circle found', 'Alien sighted', 'Abduction event', 'Rank'])
    return df


def find_rank(df, value):


    df['Rank'] = (df == value).sum(axis=1)
    return df


query = "SELECT * FROM ufo_table"
df_ufo = ufo_table_from_sql(query)
df_ufo = find_rank(df_ufo, 'Yes')
df_ufo

df_ufo.to_csv('ufo.csv', index=False)
df_ufo.to_excel('ufo.xlsx', index=False)

