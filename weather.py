#coding: utf-8
import requests
import json
import webbrowser
from jinja2 import Template
plan = open("plantilla.html","r")
capitales = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']
num_capitales = 0

html = ''
for linea in plan:
	html = html + linea
plantilla = Template(html)

lista_temp_min = []
lista_temp_max = []
lista_redon = []
lista_direccion = []

def orientacion(direccion):
	"""Función que calcula la dirección de la que procede el viento"""
	for grados in str(direccion):
		if direccion >= 337 and direccion < 22.5:
			return "N"
		elif direccion >= 22.5 and direccion < 67.5:
			return "NE"
		elif direccion >= 67.5 and direccion < 112.5:
			return "E"
		elif direccion >= 112.5 and direccion < 157.5:
			return "SE"
		elif direccion >= 157.5 and direccion < 202.5:
			return "S"
		elif direccion >= 202.5 and direccion < 247.5:
			return "SO"
		elif direccion >= 247.5 and direccion < 292.5:
			return "O"
		elif direccion >= 292.5 and direccion < 337.5:
			return "NO"

while num_capitales <= 7:
	fichero = requests.get('http://api.openweathermap.org/data/2.5/weather/',params={'q':'%s,spain' %capitales[num_capitales]})
	dicc = json.loads(fichero.text)


	temp_min = round(dicc["main"]["temp_min"] - 273)
	temp_max = round(dicc["main"]["temp_max"] - 273)
	viento = round(dicc["wind"]["speed"] * 1.61,2)
	redon = round(viento, 2)
	direccion = dicc["wind"]["deg"]

	lista_temp_min.append(temp_min)
	lista_temp_max.append(temp_max)
	lista_redon.append(redon)
	lista_direccion.append(orientacion)

	num_capitales = num_capitales + 1

plantilla_salida = plantilla.render(capitales_num=capitales,temp_min=lista_temp_min,temp_max=lista_temp_max,speed=lista_redon,direccion_viento=lista_direccion)

resultado=open('plantilla_salida.html','w')
resultado.write(plantilla_salida)
resultado.close()
webbrowser.open("plantilla_salida.html")

#print "La temparatura mínima de %s es de %s ºC, la máxima es de %s ºC\ny el viento es de %s km/h Dirección %s " % (capitales[7],temp_min,temp_max,redon,orientacion(direccion))

