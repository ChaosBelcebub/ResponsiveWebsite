#!/usr/bin/env python3
 
def application(environ, start_response):
    #status = '400 Bad Request'
    status = '200 OK'
 
    response_headers = []
    start_response(status, response_headers)
 
    return  []

