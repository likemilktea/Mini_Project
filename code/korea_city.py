import folium
from folium import plugins
import pandas as pd
import os
import numpy as np

dat=pd.read_csv("kr.csv")

df_name = dat.index
df_lati = dat['lat']   # 위도
df_long = dat['lng']  # 경도

df_lati = list(df_lati)
df_long = list(df_long)

df_loc = np.array([df_lati, df_long]).T
city_map = folium.Map(location=
                      [ np.mean( df_lati), np.mean(df_long) ], 
                       zoom_start=6)
df_name = list(df_name)
plugins.MarkerCluster(df_loc, popups=df_name).add_to(city_map)
city_map.save(os.path.join('.', 'korea_city_location.html'))
print(city_map)