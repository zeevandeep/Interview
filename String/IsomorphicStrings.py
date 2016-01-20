# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 19:52:10 2015

@author: zeevandeep
"""

class Solution:  
    # @param {string} s  
    # @param {string} t  
    # @return {boolean}  
    def isIsomorphic(self, s, t):  
        if len(s) != len(t):  
            return False  
        s_dict = {}  
        t_dict = {}  
        for i in range(len(s)):  
            if s[i] in s_dict.keys() and s_dict[s[i]] != t[i]:
                
                return False  
            if t[i] in t_dict.keys() and t_dict[t[i]] != s[i]:  
                return False  
            print s_dict
           # print s_dict[s[i]]
            print i
            #print t_dict
            s_dict[s[i]] = t[i]  
            t_dict[t[i]] = s[i]  
        return True  


s = Solution()  
#print s.isIsomorphic('app', 'bcc')
"""
print s.isIsomorphic('app', 'bc')  
print s.isIsomorphic('appasdf', 'bccb528') == True  
print s.isIsomorphic('appd3', 'bcc3r') == True  
"""
print s.isIsomorphic('appd3p', 'bcc3re')   
