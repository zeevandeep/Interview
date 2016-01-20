# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:43:32 2015

@author: zeevandeep
"""

def BinarySearchRecursion(arr,value):
    if len(arr) == 0:
        return False
    else:
        
        mid = len(arr)//2
        if arr[mid] == value:
            return True
        elif arr[mid] > value:
            return BinarySearchRecursion(arr[:mid-1],value)
        elif arr[mid] < value:
            return BinarySearchRecursion(arr[mid+1:],value)


def IndexMagicFunctionSearch(arr):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2
        if arr[mid]== mid:        
            return True
        elif arr[mid] > mid:
            return IndexMagicFunctionSearch(arr[:mid-1])
        else:
            return IndexMagicFunctionSearch(arr[mid+1:])
 


def BinarySearchDuplicatesRecursion(arr,start,end,value):
    
    
    if start > end:
        return -1
    else:
        
        mid = (start+end)//2
        if arr[mid] == mid:
            return True
        
        left_end = min(mid-1,value)
        index =  BinarySearchDuplicatesRecursion(arr,start,left_end,value)
        if index != -1:
            return "Found"
        else:
            right_start = max(mid+1,value)
            return BinarySearchDuplicatesRecursion(arr,right_start,end,value)
   
"""
index = (start + end) // 2
    value = seq[index]

    if index == value:
        return index

    # Left sub-array
    left_end = min(index - 1, value)
    left_index = magic_index_duplicates(seq, start=start, end=left_end)
    if left_index != -1:
        return left_index

    # Right sub-array
    right_start = max(index + 1, value)
    return magic_index_duplicates(seq, start=right_start, end=end)
   
 """  
print BinarySearchDuplicatesRecursion([-10,-7,-2,0,1,1,1,2,8,10],0,9,8)