#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))
c = 0
for x in xrange(0,n):
	for y in xrange(x+1,n):
		if (a[x]+a[y]) % k == 0:
			c = c + 1
print c 