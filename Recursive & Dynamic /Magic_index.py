# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:22:00 2015

@author: zeevandeep
"""

def magic_index(seq,start=None,end=None):
    if start is None:
        start=0
    if end is None:
        end =len(seq)-1
    if start > end:
        return -1
    index= (start+end)/2
    if index==seq[index]:
        return index
    if index > seq[index]:
        return magic_index(seq,start=index+1,end=end)
    else:
        return magic_index(seq,start=start,end=index-1)

def magic_loop(seq):
	arr=[]
	for index,value in enumerate (seq):
		if index == value:
			arr.append(index)
		
	#if arr:
	return arr
	#else:
	#	return "Not Found"


        
print magic_loop([23,45,23,12,6])
    
    