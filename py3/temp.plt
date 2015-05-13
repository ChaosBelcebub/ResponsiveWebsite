set title 'Temperaturverlauf'
set xlabel 'Messwert'
set ylabel 'Grad Celsius'
set yrange [-5:40]
plot 'temp-daten' using 3 with line
set output "temperatur.jpg"
set terminal jpeg
replot
