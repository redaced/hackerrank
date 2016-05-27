#!/bin/python

import sys


n = int(raw_input().strip())

arr = []
arr.append([])
for x in xrange(1,n+1):
	arr.append([])
	for j in xrange(n-x):
		arr[x].append(' ')
	for i in xrange(x):
		arr[x].append('#')

a = ""

for i in arr:
	b = False
	for l in i:
		if l != None:
			a += l
			b = True
	if b:
		a += "\n"

print a