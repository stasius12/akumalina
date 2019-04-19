#!/usr/bin/env gnuplot
set terminal png size 1024,768
set output "static/test.png"

set ylabel "wartość"
set xlabel "czas (s)"
set xdata time
set timefmt "%H:%M"
set format x "%H:%M"
set grid
plot "temperatures/data_temp.dat" using 1:2 with lines lc rgbcolor "#ff0000" title "temperatura" 

