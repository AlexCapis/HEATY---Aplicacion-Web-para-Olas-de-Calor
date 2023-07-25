import requests
from pprint import pprint

# Preguntar la ciudad en la que queremos que se nos dé el tiempo
# city = input("Enter your city:  ") 
# usamos units=metric para pasar las unidades de medida Americanas a las Europeas .format(city)
url = "https://api.openweathermap.org/data/2.5/weather?q=Madrid&appid=25d56b99caf2b32642d78f1880994805&units=metric" #https://openweathermap.org

# Enviamos a la API la url con la ciudad para que sea analizada
res = requests.get(url)

# Para que a información que nos de la API sea en formato json
data = res.json()


temp = data["main"]["temp"] # dentro del diccionario de main está temp
vel_viento = data["wind"]["speed"] # dentro del diccionario de wind está speed

latitud = data["coord"]["lat"] # dentro del diccionario coord está lat
longitud = data["coord"]["lon"] # dentro de coord está lon

descripcion = data["weather"][0]["description"] # description es diferente ya que es un diccionario dentro de una lista por eso ponemos [0]

# Imprimimos el valor de cada variable
'''
print("Tempreratura: ", temp)
print("Velocidad del viento: {} m/s".format(vel_viento))
print("Latitud: {}".format(latitud))
print("Longitud: {}".format(longitud))
print("Descripción: {}".format(descripcion))
'''
pprint(data)