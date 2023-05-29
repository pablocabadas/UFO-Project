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

def add_location_data(df):
    geolocator = Nominatim(user_agent="my_code")
    location_list = []

    for i in df.location:
        coordinates = i
        location = geolocator.reverse(coordinates)
        location_list.append(location.raw)

    province_list = []
    state_list = []
    hamlet_lat_list = []
    hamlet_lon_list = []
    for i in location_list:
        try:
            province = i['address']['state_district']
            state = i['address']['state']
            hamlet_lat = i['lat']
            hamlet_lon = i['lon']

            province_list.append(province)
            state_list.append(state)
            hamlet_lat_list.append(hamlet_lat)
            hamlet_lon_list.append(hamlet_lon)

        except:
            try:
                province = i['address']['province']
                state = i['address']['state']
                hamlet_lat = i['lat']
                hamlet_lon = i['lon']

                province_list.append(province)
                state_list.append(state)
                hamlet_lat_list.append(hamlet_lat)
                hamlet_lon_list.append(hamlet_lon)
            except:
                try:
                    province = "nan"
                    state = "nan"
                    hamlet_lat = "nan"
                    hamlet_lon = "nan"

                    province_list.append(province)
                    state_list.append(state)
                    hamlet_lat_list.append(hamlet_lat)
                    hamlet_lon_list.append(hamlet_lon)
                except:
                    continue

    df_location = pd.DataFrame({'province': province_list, 'state': state_list, 'hamlet location': list(zip(hamlet_lat_list, hamlet_lon_list))})

    all_ufo = pd.concat([df, df_location], axis=1)

    return all_ufo

all_ufo = add_location_data(df_ufo)
all_ufo

all_ufo.to_excel('all_ufo.xlsx', index=False)