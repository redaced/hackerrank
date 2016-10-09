#!/bin/python

import sys


T = int(raw_input().strip())

for x in xrange(0,T):
	U = ''
	S = raw_input().strip()
	for i in xrange(0,len(S),2):
		U += S[i]	
	U += ' '
	for j in xrange(1,len(S),2):
		U += S[j]
	print U
print "\n"