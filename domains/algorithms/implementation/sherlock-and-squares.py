#!/bin/python

import sys,math

t = int(raw_input().strip())
for a0 in xrange(t):
    a,b = raw_input().strip().split(' ')
    a,b = [int(a),int(b)]
    print int(math.floor(math.sqrt(b)) - math.floor(math.sqrt(a - 1)))