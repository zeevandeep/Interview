# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 15:05:44 2015

@author: zeevandeep
"""

def rever(para):
    a=len(para)
    word=''
    while a>0:
        word+=para[a-1]
        a-=1
        print a
    return word
        
print rever('hello')