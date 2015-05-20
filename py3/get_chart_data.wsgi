#!/usr/bin/env/python3

import datetime
import time
import sqlite3 as lite

def application(environ, start_response):

	status = '400 Bad Request'
	output = ''
	con = lite.connect('/var/www/py3/temperatur.db')

	actual_date = datetime.date.today()
	check_date = actual_date - datetime.timedelta(days=100)

	with con:
		status = '200 OK'
		cur = con.cursor()

		while check_date != actual_date + datetime.timedelta(days=1):
			hour = 0
			while hour < 24:
				cur.execute("Select * from temp where date = '" + check_date.strftime('%d %m %Y') + "' and hour = " + str(hour) + " limit 1")
				result = cur.fetchone()

				if result == None:
					output += "null"
				else:
					output += str(result[2])

				if (check_date != actual_date or hour != 23):
					output += ","

				# output += check_date.strftime('%d %m %Y') + ' ' + str(hour) + '\n'
				hour += 1

			check_date = check_date + datetime.timedelta(days=1)

	response_body = output

	response_headers = [('Content-Type', 'text/plain'),
						('Content_Length', str(len(response_body)))]

	start_response(status, response_headers)
 
	return [response_body]