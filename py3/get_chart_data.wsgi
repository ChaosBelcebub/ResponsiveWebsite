#!/usr/bin/env/python3

import sqlite3 as lite

def application(environ, start_response):

	status = '200 OK'
	output = 'Test'

	response_body = output

	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]