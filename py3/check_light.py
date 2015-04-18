#!/usr/bin/env/python3

import subprocess
from cgi import parse_qs, escape

def application(environ, start_response):

	d = parse_qs(environ['QUERY_STRING'])

	room = d.get('room', [''])[0]
	room = excape(room)
	response_body = str(room)
	#if subprocess.check_output(["gpio", "-g", "read", "17"]) == b'1\n':
	#	response_body = 'True'
	#else:
	#	response_body = str(subprocess.check_output(["gpio", "-g", "read", "17"]))
	
	#status = '400 Bad Request'
	status = '200 OK'
    
	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]

