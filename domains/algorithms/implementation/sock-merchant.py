#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
c = sorted(c)
count = 0
for x in xrange(0,n):
	for y in xrange(x+1,n):
		if c[x] == c[y]:
			count=count+1
			c[x] = -1
			c[y] = -1
print count