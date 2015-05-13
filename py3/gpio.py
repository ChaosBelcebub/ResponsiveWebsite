#!/usr/bin/env python

from subprocess import call
import grovepi
import sqlite3 as lite
import time
import os


def pset(pin, value):
	call(["gpio", "-g", "write", str(pin), str(value)])


pins = [17, 18]

with open('/var/www/py3/options', 'w') as f: 
	f.write('18.0')
f.close()

with open('/var/www/py3/temperature', 'w') as f: 
	f.write('18.0')
f.close()

for pin in pins:
	call(["gpio", "export", str(pin), "out"])

sensor_value = 450 # Der Sensorwert wird mit "450" initialisiert
sensor_value_prev = 450 # Der vorherige Sensorwert wird mit "450" initialisiert

hour = time.strftime('%H')
hour_prev = hour
con = lite.connect('/var/www/py3/temperatur.db')

light_sensor = 0 # Der Lichtsensor wird mit "0" initialisiert, da er an dem analogen (GrovePi) Anschluss "0" angeschlossen ist
grovepi.pinMode(light_sensor, "INPUT")

sensor = 1 # Der Temperatursensor wird mit "1" initialisiert, da er an dem analogen (GrovePi) Anschluss "1" angeschlossen ist
relais = 2 # Das Relais wird mit "2" initialisiert, da es an dem digitalen (GrovePi) Anschluss "2" angeschlossen ist
option = 0.0
grovepi.pinMode(relais,"OUTPUT")
temp = 0.0

while True:
	time.sleep(0.5)
	try:
		temp = grovepi.temp(sensor,'1.1')
	
		with open('/var/www/py3/temperature', 'w') as f:
			f.write(str(round(temp,1))) # Die aktuelle Temperatur wird gerundet auf eine Nachkommastelle in die Textdatei "temperature" als String reingeschrieben
		f.close
	except:
		pass

	try:
		sensor_value = grovepi.analogRead(light_sensor)
		
	except:
		pass

	if(sensor_value < 430 and sensor_value_prev >= 430):
		for pin in pins:
			pset(pin, 1)
	elif(sensor_value > 430 and sensor_value_prev <= 430):
		for pin in pins:
			pset(pin, 0)

	sensor_value_prev = sensor_value

	try:
		with open('/var/www/py3/options', 'r') as f:
			option = float(f.read())
		f.close()

		if(temp < option):
			grovepi.digitalWrite(relais,1)
		else:
			grovepi.digitalWrite(relais,0)
	except:
		grovepi.digitalWrite(relais,0)
	
	hour = time.strftime('%H')

	try:
		if (hour != hour_prev):
			with con:
				cur = con.cursor()
				cur.execute("insert into temp values('" + time.strftime('%d %m %Y') + "'," + time.strftime('%H') + ",'" + str(round(temp, 1)) + "')")
	except:
		print("error")
	hour_prev = hour
	
	#try:
	#	Zeit = time.strftime('%Y-%m-%d %H:%M:%S')
	#	

	#	with open('/var/www/py3/temp-daten', 'a') as f:
	#		f.write(Zeit +' '+ str(round(temp,1))+'\n' )
	#	f.close()	
	#	
	#		
	#			
	#	#os.system('gnuplot /var/www/py3/temp.plt')
	#	
	#except:
	#	pass	
