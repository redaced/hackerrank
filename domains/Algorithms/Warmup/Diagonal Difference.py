#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

fd = 0
sd = 0
c = n - 1
for x in xrange(n):
	fd += a[x][x]
	sd += a[x][c]
	c -= 1	
print abs(fd - sd)