#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

for x in xrange(0,n):
	if (ord(s[x]) >= 65 and ord(s[x]) <= 90) or (ord(s[x]) >= 97 and ord(s[x]) <= 122) :
		print chr(ord(s[x]) + k),