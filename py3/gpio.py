#!/usr/bin/env python

from subprocess import call

pins = [17, 18]

with open('options', 'w') as f:
	f.write('18.0')
f.close()

for pin in pins:
	call(["gpio", "export", str(pin), "out"])
