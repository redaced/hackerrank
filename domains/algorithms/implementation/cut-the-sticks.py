#!/bin/python

import sys

def ff(ar,mi):
	s = 0
	for x in xrange(0, len(ar), +1):
		if ar[x] > 0:
			ar[x] -= mi
			s += 1
	return ar,s

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
a = sum(arr)
while a > 0:
	arr,t = ff(arr,min(i for i in arr if i > 0))
	a = sum(arr)
	print t