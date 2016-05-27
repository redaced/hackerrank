#!/bin/python

import sys

def mns(i,n):
	print round((float(i) / n),6)

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
positive = 0
negative = 0
zero = 0
for x in arr:
	if x > 0:
		positive += 1
	elif x == 0:
		zero += 1
	else:
		negative += 1
mns(positive,n)
mns(negative,n)
mns(zero,n)	