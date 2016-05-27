#!/bin/python

import sys

def kaprekar(i):
	if i == 1:
		return i
	if i > 5:
		sqr = i * i
		strs = str(sqr)
		half = len(strs) / 2
		fh = ''
		for x in xrange(0, half):
			fh += strs[x]
		sh = ''
		for x in xrange(half, len(strs)):
			sh += strs[x]
		if (int(fh) + int(sh)) == i:
			return i

p = int(raw_input().strip())
q = int(raw_input().strip())

res = []
for i in xrange(p,q+1):
	res.append(kaprekar(i))
printer = True
for i in res:
	if i != None:
		printer = False
		print i,
if(printer):
	print "INVALID RANGE"