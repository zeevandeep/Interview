# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:02:44 2015

@author: zeevandeep
"""

def fibonacci(n):
    ans=1
    k=0
    c=0
    for i in range(n):
       ans+=c
       c=k   
       k=ans
       print ans
       
     
#print fibonacci(5)     

def recursivefibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recursivefibonacci(n-1) + recursivefibonacci(n-2)

print fibonacci(6)