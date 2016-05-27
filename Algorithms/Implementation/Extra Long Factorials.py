#!/bin/python

import sys

def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))
n = int(raw_input().strip())

print factorial(n)