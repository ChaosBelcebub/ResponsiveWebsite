#!/usr/bin/env python

from subprocess import call

pins = [17, 18]

for pin in pins:
	print "gpio export " + str(pin) + " out"
	call(["gpio", "export", str(pin), "out"])
