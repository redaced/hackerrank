#!/bin/python

import sys
import math

strings = raw_input()
a = math.sqrt(len(strings))

ceil = math.ceil(a)

arr = [[]]
c = 0

for x in xrange(1,int(ceil)):
	arr.append([])

for x in strings:
	if c > int(ceil) - 1:
		c = 0
	arr[c].append(x)
	c = c + 1

a = ""
for i in arr:
	for l in i:
		a += l
	a += " "

print a