# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:12:01 2015

@author: zeevandeep
"""

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        if s == '' or s == '(' or s == ')':
            return 0
        stack = [')']
        maxLen = 0
        for i in xrange(len(s)):
            if s[i] == ')' and stack[-1] == '(':
                stack.pop()
                #print maxLen                
                maxLen+=2
                
            else:
                stack.append(s[i])
        return maxLen
#test
s = Solution()
print s.longestValidParentheses("(()")
print s.longestValidParentheses('(()()()')
print s.longestValidParentheses(')()())')