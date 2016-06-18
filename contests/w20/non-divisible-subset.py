#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
c = 0
for x in xrange(0,len(a)):
	for y in xrange(x+1, len(a)):
		if (a[x] + a[y]) % k != 0:
			c += 1
print c