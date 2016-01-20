# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 15:47:04 2015

@author: zeevandeep
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        ans = 0
        number = str(n)
        while ans!=1:
            for i in number:
                square = int (i)* int(i)
                ans+=square
                
            if ans == 1:
                return True
            else:
                return self.isHappy(ans)
a =Solution()
print a.isHappy(95)