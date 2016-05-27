#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
    i,j = raw_input().strip().split(' ')
    i,j = [int(i),int(j)]
    mini = width[i]
    for x in xrange(i, j+1):
    	if width[x] < mini :
    		mini = width[x]
    print mini