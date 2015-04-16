#!/usr/bin/env python3

def application(environ, start_response):
	response_body = 'True'
	
    #status = '400 Bad Request'
	status = '200 OK'
    
	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]