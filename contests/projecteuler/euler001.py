#!/bin/python

import sys

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    p = (n-1)/3
    sus = ((3*p*(p+1))/2)
    p = (n-1)/5
    sus = sus + ((5*p*(p+1))/2)
    p = (n-1)/15
    sus = sus - ((15*p*(p+1))/2)
    print sus