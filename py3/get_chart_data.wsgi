#!/usr/bin/env/python3

import json
import datetime
import time
import sqlite3 as lite

def application(environ, start_response):

	status = '400 Bad Request'
	output = []
	con = lite.connect('/var/www/py3/temperatur.db')

	with con:
		cur = con.cursor()
		cur.execute("Select * from temp order by rowid asc")

		while True:
			row = cur.fetchone()

			if row == None:
				break

			#output += str(row[0]) + ' - ' + str(row[1]) + ',' + str(row[2]) + '\n'
			#output += '2015' + ',' + str(row[2]) + '\n'
			date = str(row[0]) + ' - ' + str(row[1]) + ' Uhr'
			element = [date, float(row[2])]
			output.append(element)
		status = '200 OK'
	
	output = json.dumps(output)
	response_body = output

	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]