#!/bin/python

import sys

def datee(hrs,mins):
  words=["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", "twenty five", 
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
  msg=""
  if (hrs >12):
      hrs=hrs-12
  if (mins == 0):
      hr = words[hrs-1]
      msg = hr + " o' clock"
  elif (mins == 30 or mins == 15):
      hr = words[hrs-1]
      mn = words[mins-1]
      msg = mn + " past " + hr
  elif (mins < 31):      
      hr = words[hrs-1]
      mn = words[mins-1]
      msg = mn + " minutes past " + hr
  elif (mins == 45):
      hr = words[hrs]
      mn = words[(60 - mins-1)]
      msg = mn + " to " + hr
  else:
      hr = words[hrs]
      mn = words[(60 - mins-1)]
      msg = mn + " minutes to " + hr
  print msg

h = int(raw_input().strip())
m = int(raw_input().strip())

datee(h,m)