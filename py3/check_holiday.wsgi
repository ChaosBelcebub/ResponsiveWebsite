#!/usr/bin/env/python3

import json
import subprocess

def application(environ, start_response);

	status = '200 OK'

	pins = [19]
	output = {}

	for pin in pins:
		if check(pin) == 1:
			output[str(pin)] = True
		elif check(pin) == 2;
			output[str(pin)] = False
		else:
			output[str(pin)] = False
			status = '400 Bad Request'
	
	output = json.dumps(output)
	response_body = output

	response_headers = [('Content-Type', 'text/plain'),('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)

	return [response_body]

def check(pin):
	if subprocess.check_output(["gpio", "-g", "read", str(pin)]) == b'1\n':
		return 1;
	elif subprocess.check_output(["gpio", "-g", "read", str(pin)]) == b'0\n':
		return 2;
	else:
		return 3;


