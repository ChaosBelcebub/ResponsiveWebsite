#!/usr/bin/env python

from subprocess import call
import grovepi
import sqlite3 as lite
import time
import os
import pygal
from pygal.style import LightStyle


def pset(pin, value):
	call(["gpio", "-g", "write", str(pin), str(value)])

def check(pin):
	if subprocess.check_output(["gpio", "-g", "read", str(pin)]) == b'1\n':
		return True;
	elif subprocess.check_output(["gpio", "-g", "read", str(pin)]) == b'0\n':
		return False;
	else:
		return False;


output = [17, 18]
inpu = [22, 23]

with open('/var/www/py3/options', 'w') as f: 
	f.write('18.0')
f.close()

with open('/var/www/py3/temperature', 'w') as f: 
	f.write('18.0')
f.close()

# Initalisiere in und ouput pins
for pin in output:
	call(["gpio", "export", str(pin), "out"])

for pin in inpu:
	call(["gpio", "export", str(pin), "in"])

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
		for pin in output:
			pset(pin, 1)
	elif(sensor_value > 430 and sensor_value_prev <= 430):
		for pin in output:
			pset(pin, 0)

	sensor_value_prev = sensor_value

	try:
		with open('/var/www/py3/options', 'r') as f:
			option = float(f.read())
		f.close()

		# Vergleiche Temperaturen und pruefe Magnetschalter
		if(temp < option and check(22) and check(23)):
			grovepi.digitalWrite(relais,1)
		else:
			grovepi.digitalWrite(relais,0)
	except:
		grovepi.digitalWrite(relais,0)

	hour = time.strftime('%H')

	label = []
	data = []

	if (hour != hour_prev):
		try:
			# Verbindung zu SQLite Datenbank
			with con:
				# Schreiben
				cur = con.cursor()
				cur.execute("insert into temp values('" + time.strftime('%d %m %Y') + "'," + time.strftime('%H') + ",'" + str(round(temp, 1)) + "')")
				# Lesen
				cur = con.cursor()
				cur.execute("select * from (SELECT rowid, date, hour, t FROM temp order by rowid desc limit 48) order by rowid asc")

				while True:
					row = cur.fetchone()

					if row == None:
						break;

					label.append(str(row[1]) + ' - ' + str(row[2]) + ' Uhr')
					data.append(float(row[3]))
		except:
			print("Database error")

		# Erstelle neues Chart
		chart = pygal.Line(x_label_rotation=45, x_labels_major_count=12, show_minor_x_labels=True, show_legend=False, no_data_text='Keine Daten gefunden', truncate_label=25, style=LightStyle)
		chart.title = 'Temperaturverlauf der letzten 48 Messungen'
		chart.x_labels = label
		chart.add('Temperatur', data)
		chart.render_to_file('chart.svg')

	hour_prev = hour