#!/usr/bin/env/python3

import os, sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/wiringpi-1.1.0-py2.7-linux-armv6l.egg/wiringpi.pyc')

import wiringpi

io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
io.pinMode(17,io.OUTPUT)

def application(environ, start_response):
	if io.digitalRead(17) == 1:
		response_body = 'True'
	else:
		response_body = 'False'
	
	#status = '400 Bad Request'
	status = '200 OK'
    
	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]

