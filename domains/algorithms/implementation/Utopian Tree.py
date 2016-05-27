#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    height = 1
    if n != 0:
    	for x in xrange(1,n+1):
    		if x % 2 != 0:
    			height += height
    		else:
    			height += 1
    print height