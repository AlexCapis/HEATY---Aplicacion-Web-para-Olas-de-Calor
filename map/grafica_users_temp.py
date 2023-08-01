import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import requests


'''
se cargan los datos de los usuarios registrados "csv/usuarios_logueados.csv" y se utiliza la fecha para representarlo frente al tiempo
Tambien se hace una llamada a la api de la AEMET para representar la temperatura media diaria

Se busca ver si el aumento de las temperaturas favorece al registro de mas usuario.

'''

# Importar datos usuarios logueados
df_us = pd.read_csv('./users_login/users.csv')
df_us["fecha_registro"] = pd.to_datetime(df_us["fecha_registro"],format="%d-%m-%Y")
# print(df_us.head())

#  API AEMET. temperatura media diaria de Madrid
#Podemos seleccionar el rango de las fechas que nos interesa. Esta para que coja la fecha_fin sea la actual
fecha_inicio = "2023-01-01"
fecha_fin = time.strftime("%Y-%m-%d")

api_key = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqYW1lbmRpYmFyQGdtYWlsLmNvbSIsImp0aSI6IjMwYWMzZWU0LWMwNDItNDM0NS1iY2YzLTAxNWEwMDBmZTQyMyIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNjkwMjk3MjE1LCJ1c2VySWQiOiIzMGFjM2VlNC1jMDQyLTQzNDUtYmNmMy0wMTVhMDAwZmU0MjMiLCJyb2xlIjoiIn0.qgV8yNMpKsAFrnFGphnPwtf4w_IyyRvC9QOro75LTzM'
url = f'https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{fecha_inicio}T00:00:00UTC/fechafin/{fecha_fin}T00:00:00UTC/estacion/3195/?api_key={api_key}'
response = requests.get(url)
data = response.json()
enlace_datos = data['datos']
response = requests.get(enlace_datos)
data = response.json()
# Crea una lista
fecha = [registro['fecha'] for registro in data]
temp_media = [registro['tmed'] for registro in data]
# DATAFRAME de la temperatura
df_temp = pd.DataFrame({'Fecha': fecha, 'Ta Media C': temp_media})
# Convierte la columna 'Fecha' a tipo datetime para la grafica
df_temp['Fecha'] = pd.to_datetime(df_temp['Fecha'])
# print(df_temp.head())


# REPRESENTACION DE NUEVOS USUARIOS POR FECHA (AZUL) Y MEDIA DE TMP DIARIA POR DIA (COLORADO)
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

df_grouped = df_us.groupby("fecha_registro").size().reset_index(name="registros")

# Establece "fecha de registro" como el índice para el plot
df_grouped.set_index("fecha_registro", inplace=True)

ax1.plot(df_grouped.index, df_grouped["registros"], color='b',label="Número de registros")
ax1.set_ylabel("Número de registros")
ax1.set_ylim(bottom=0)
# df_temp
ax2.plot(df_temp["Fecha"], df_temp["Ta Media C"], color="r", label="Temperatura Diaria")
ax2.set_ylabel("Temperatura Diaria (ºC)")
# ax2.set_ylim(0, 40)
ax1.set_xlabel("Fecha")
ax1.set_title("Número de Registros y Temperatura Diaria")
ax1.grid(True)
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()