#!/usr/bin/env/python3

import json
import subprocess

def application(environ, start_response);

    status = '200 OK'

    output = {}

    try:
        with open('/var/www/py3/holiday', 'r') as f:
            output['holiday'] = f.read()
    except:
        status = '400 Bad Request'
    else:   
        f.close()
    
    output = json.dumps(output)
    response_body = output

    response_headers = [('Content-Type', 'text/plain'),('Content_Length', str(len(response_body)))]

    start_response(status, response_headers)

    return [response_body]