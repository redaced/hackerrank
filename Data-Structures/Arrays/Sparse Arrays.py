#!/bin/python

import sys

n = int(raw_input().strip())
strings = []
for arr_i in xrange(n):
    arr_temp = raw_input()
    strings.append(arr_temp)

q = int(raw_input().strip())
queries = []
for i in xrange(q):
	arr_temp = raw_input()
	queries.append(arr_temp)

for x in xrange(q):
	s = 0
	if queries[x] in strings:
		for i in xrange(n):
			if queries[x] == strings[i]:
				s = s + 1
	print s