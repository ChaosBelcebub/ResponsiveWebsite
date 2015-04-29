#!/usr/bin/env/python3

import json
import subprocess

import sys, os

import grovepi

def application(environ, start_response):

	status = '200 OK'

	output = {}

	# check the temperature:

	output['sensor'] = '22.5'

	with open('options', 'r') as f:
		output['option'] = f.read()
	f.close()

	output = json.dumps(output)
	response_body = output

	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]
