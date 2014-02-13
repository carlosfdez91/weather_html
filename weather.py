#coding: utf-8
import requests
import json
import jinja2

capitales = ["Almería","Cádiz","Córdoba","Granada","Huelva","Jaén","Málaga","Sevilla"]

respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % capitales[0]})

dicc = json.loads(respuesta.text)

tempmin = dicc["main"]["temp_min"] - 273
tempmax = dicc["main"]["temp_max"] - 273
viento = dicc["wind"]["speed"]

print "La temparatura mínima de %s es de %s ºC, la máxima es de %s ºC\ny el viento es de %s km/h " % (capitales[0],tempmin,tempmax,viento)