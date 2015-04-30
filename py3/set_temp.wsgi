#!/usr/bin/env/python3

import json
import subprocess
from cgi import parse_qs, escape

def application(environ, start_response):

	status = '200 OK'
	d = parse_qs(environ['QUERY_STRING'])
	value = d.get('value', [''])[0]
	value = escape(value)

	output = {}

	try:
		with open('/var/www/py3/options', 'w') as f:
			f.write(str(value))
	except:
		status = '400 Bad Request'
	else:	
		f.close()

	output = json.dumps(output)
	response_body = output

	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]
