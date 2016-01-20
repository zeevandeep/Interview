# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:26:21 2015

@author: zeevandeep
"""

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def my_cmp(x,y):
            sx = str(x)
            sy = str(y)
            sx = sx + sy
            sy = sy + sx
            if sx > sy:
                return -1
            if sx == sy:
                return 0
            if sx < sy:
                return 1
            
        nums = sorted(nums, cmp=my_cmp)
         
        if nums[0] == 0:
            return "0"
        else:
            return "".join([str(n) for n in nums])
a=Solution()
print a.largestNumber([2,3,5,6,60])