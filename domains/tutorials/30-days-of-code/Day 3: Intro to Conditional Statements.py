#!/bin/python

import sys


N = int(raw_input().strip())
if N == 2 or N == 4:
	print "Not Weird"
elif N > 6 and N < 21:
	print "Weird"
elif N % 2 != 0:
	print "Weird"
else:
	print "Not Weird"