#!/bin/python
 
import sys
 
cost = float(raw_input().strip())
tip = int(raw_input().strip())
tax = int(raw_input().strip())

print "The total meal cost is",int(round(cost + (cost * (tip/100.0)) + (cost * (tax/100.0)))),"dollars."