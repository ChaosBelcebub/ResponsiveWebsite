#!/usr/bin/env python

from subprocess import call
import grovepi
import time 

pins = [17, 18]

with open('/var/www/py3/options', 'w') as f:
	f.write('18.0')
f.close()

with open('/var/www/py3/temperature', 'w') as f:
	f.write('18.0')
f.close()

for pin in pins:
	call(["gpio", "export", str(pin), "out"])

sensor_value = 450
sensor_value_prev = 450

light_sensor = 0
grovepi.pinMode(light_sensor, "INPUT")

sensor = 1

while True:
	time.sleep(0.5)
	try:
		temp = grovepi.temp(sensor,'1.1')
	
		with open('/var/www/py3/temperature', 'w') as f:
			f.write(str(round(temp,1)))
		f.close()
	except:
		pass

	try:
		sensor_value = grovepi.analogRead(light_sensor)
		
	except:
		pass

	if(sensor_value < 400 and sensor_value_prev >= 400):
		for pin in pins:
			pset(pin, 1)
	elif(sensor_value > 400 and sensor_value_prev <= 400):
		for pin in pins:
			pset(pin, 0)

	sensor_value_prev = sensor_value

def pset(pin, value):
	subprocess.call(["gpio", "-g", "write", str(pin), str(value)])
