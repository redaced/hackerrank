#!/bin/python

import sys
from datetime import datetime

time = raw_input().strip()

date = datetime.strptime(time, '%I:%M:%S%p')
print date.strftime('%H:%M:%S')