#!/bin/python

import sys


a=0
items=[]

a=int(raw_input(''))
for i in range(0,a):
    items.append(int(raw_input('')))



def Sherlock_and_The_Beast(items):
    for i in items:

        if i<3:
            print -1
        elif i%3==0:
            print int(str(5)*i)
        elif i==5:
            print int(str(3)*i)

        else:
            flag=False
            for j in range(i/3,-1,-1):
                if (i-(3*j))%5==0:
                    flag=True
                    print int(str(5)*(3*j)+str(3)*(i-(3*j)))
                    break
            if not flag:
                print -1




Sherlock_and_The_Beast(items)