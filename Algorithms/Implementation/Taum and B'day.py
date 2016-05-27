#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]

    cost = 0
    if (z > x and z > y) or (z == x and z == y):
    	cost = cost + x * b
    	cost = cost + y * w
    else:
    	if x > y and z + y < x:
    		cost = cost + (z + y) * b 
    		cost = cost + y * w
    	elif y > x and x + z < y:
    		cost = cost + x * b 
    		cost = cost + (x + z) * w
    	else:
    		cost = cost + x * b
    		cost = cost + y * w
    print cost