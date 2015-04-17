#!/usr/bin/env/python3

import subprocess

def application(environ, start_response):
	if subprocess.check_output(["gpio", "-g", "read", "17"]) == b'1\n':
		response_body = 'True'
	else:
		response_body = str(subprocess.check_output(["gpio", "-g", "read", "17"]))
	
	#status = '400 Bad Request'
	status = '200 OK'
    
	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]

