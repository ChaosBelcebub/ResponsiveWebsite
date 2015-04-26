#!/usr/bin/env/python3

import json
import subprocess
import option

def application(environ, start_response):

	status = '200 OK'

	output = {}

	# check the temperature:
	# subprocess.check_output(["gpio", "-g", "read", str(pin)]) == b'1\n':

	output['sensor'] = 22.5
	output['option'] = options.temperature

	output = json.dumps(output)
	response_body = output

	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]