import pandas as pd
from functions1 import *

df_air_quality = pd.read_csv('https://raw.githubusercontent.com/freeja/id2223-project/master/london-air-quality.csv')
print(df_air_quality.head())

df_air_quality['city'] = "London"

df_air_quality.date = df_air_quality.date.apply(timestamp_2_time)
df_air_quality.sort_values(by = ['date'], inplace = True, ignore_index = True)

df_weather = pd.read_csv('https://raw.githubusercontent.com/freeja/id2223-project/master/london-weather.csv')

df_weather.date = df_weather.date.apply(timestamp_2_time)
df_weather.sort_values(by=['date'], inplace=True, ignore_index=True)

df_weather.head()

df_weather = df_weather.drop(columns=["precipprob", "uvindex"])

import hopsworks
project = hopsworks.login()

fs = project.get_feature_store() 

air_quality_fg = fs.get_or_create_feature_group(
        name = 'lond_air_quality_fg',
        description = 'Air Quality characteristics of each day',
        version = 1,
        primary_key = ['city','date'],
        online_enabled = True,
        event_time = 'date'
    )    
air_quality_fg.insert(df_air_quality)

weather_fg = fs.get_or_create_feature_group(
        name = 'lond_weather_fg',
        description = 'Weather characteristics of each day',
        version = 1,
        primary_key = ['city','date'],
        online_enabled = True,
        event_time = 'date'
    )
weather_fg.insert(df_weather)
