#coding: utf-8
import requests
import json
import webbrowser
from jinja2 import Template
plantilla = open("plantilla.html","r")

html = ''

for linea in html:
	html += linea

miplantilla = Template(html)
miplantilla.render(capitales='capital',temp_min='temp_min',temp_max='temp_max',viento='redon',orientacion='direccion_viento')

print html
fresultado = open('resultado.html','w')
fresultado.write('miplantilla')

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

for elemento in capitales:
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % elemento})
	dicc = json.loads(respuesta.text)
	temp_min = dicc["main"]["temp_min"] - 273
	temp_max = dicc["main"]["temp_max"] - 273
	viento = round(dicc["wind"]["speed"] * 1.61,2)
	redon = round(viento, 2)
	direccion = dicc["wind"]["deg"]

webbrowser.open("resultado.html")

#print "La temparatura mínima de %s es de %s ºC, la máxima es de %s ºC\ny el viento es de %s km/h Dirección %s " % (capitales[7],temp_min,temp_max,redon,orientacion(direccion))

