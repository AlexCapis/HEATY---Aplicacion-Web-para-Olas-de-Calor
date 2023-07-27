import folium
import pandas as pd
from geopy.geocoders import Nominatim
import re

"""
Genera un mapa de madrid con unas chinchetas segun las coordenads de los CP

Hay que hacer que represente el sumatorio de usuarios por CP y aparezcan en el mapa las chinchetas con un numero segun
los usuarios de la zona

"""


# Carga la tabla de coordenadas y CP para poder ubicar las chinchetas, y los transforma en 3 listas para usarlo en el FoliumMpa
df_coord_cp = pd.read_csv('./csv/tabla_coord_cp.csv')
numeros = df_coord_cp['Codigo Postal'].tolist()
coordenadas_long = df_coord_cp['Coord_long'].tolist()
coordenadas_latit = df_coord_cp['Coord_lat'].tolist()
# df_coord_cp.head()


# Crear el Mapa y arranca sobre Madrid con un zoom de 12
mapa = folium.Map(location=[40.429628, -3.687435], zoom_start=12)

# Agregar marcadores para cada código postal y sus coordenadas
# esto es lo que hay que cambiar, para que meta un sumatorio de los dif CP y los ubique macheando con la tabla_coord_cp.csv
for cp, lon, alt in zip(numeros, coordenadas_long, coordenadas_latit):
    folium.Marker(
        location=[alt, lon],
        popup=f'Postal Code: {cp}, Latitud: {alt}, Longitud: {lon}'      
    ).add_to(mapa)

# Genera un mapa de Madrid con unas chinchetas en las zonas de los codigos postales
mapa.save('mapa_ub_cpostales.html')