#!/bin/python

import sys,math


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]

    total = wrappers = n / c
    while wrappers >= m:
	 
		trade = wrappers / m
		total = total + trade
		wrappers = wrappers % m
		wrappers = wrappers + trade

    print total