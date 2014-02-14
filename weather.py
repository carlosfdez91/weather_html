#coding: utf-8
import requests
import json
from jinja2 import Template
plantilla = open("plantilla.html","w")

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

capitales = ["Almería","Cádiz","Córdoba","Granada","Huelva","Jaén","Málaga","Sevilla"]

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % capitales[7]})

dicc = json.loads(respuesta.text)

tempmin = dicc["main"]["temp_min"] - 273
tempmax = dicc["main"]["temp_max"] - 273
viento = dicc["wind"]["speed"] * 1.61
redon = round(viento, 2)
direccion = dicc["wind"]["deg"]

print "La temparatura mínima de %s es de %s ºC, la máxima es de %s ºC\ny el viento es de %s km/h Dirección %s " % (capitales[7],tempmin,tempmax,redon,orientacion(direccion))

