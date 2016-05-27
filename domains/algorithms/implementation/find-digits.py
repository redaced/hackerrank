#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    nstr = str(n)
    c=0
    for x in nstr:
    	if int(x) != 0:
	    	if n % int(x) == 0:
	    		c += 1
    print c