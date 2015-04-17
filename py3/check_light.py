#!/usr/bin/env/python3

import wiringpi
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
io.pinMode(17,io.OUTPUT)

def application(environ, start_response):
	if io.digitalRead(17) == 1:
		response_body = 'True'
		print "juhu"
	else:
		response_body = 'False'
	
	#status = '400 Bad Request'
	status = '200 OK'
    
	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]

