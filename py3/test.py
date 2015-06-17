import sqlite3 as lite
import pygal
from pygal.style import LightStyle
import time
import os

con = lite.connect('/var/www/py3/temperatur.db')

while True:
	time.sleep(5)
	label = []
	data = []

	with con:
		# Lesen
		cur = con.cursor()
		cur.execute("select * from (SELECT rowid, date, hour, t FROM temp order by rowid desc limit 48) order by rowid asc")

		while True:
			row = cur.fetchone()

			if row == None:
				break;

			label.append(str(row[1]) + ' - ' + str(row[2]) + ' Uhr')
			data.append(float(row[3]))
	print("start")
	chart = pygal.Line(x_label_rotation=45, x_labels_major_count=12, show_minor_x_labels=True, show_legend=False, no_data_text='Keine Daten gefunden', truncate_label=25, style=LightStyle)
	chart.title = 'Temperaturverlauf der letzten 48 Messungen'
	chart.x_labels = label
	chart.add('Temperatur', data)
	chart.render_to_file('chart.svg')
	os.rename("chart.svg", "../chart.svg")
	print("end")
