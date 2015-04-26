#!/usr/bin/env python

from subprocess import call
import option

pins = [17, 18]

option.init()

for pin in pins:
	print "gpio export " + str(pin) + " out"
	call(["gpio", "export", str(pin), "out"])
