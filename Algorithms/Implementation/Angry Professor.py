#!/bin/python
 
import sys
 
 
t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    t = 0
    for i in a:
        if i <= 0:
            t+=1
           
    if k > t:
        print 'YES'
    else:
        print 'NO'