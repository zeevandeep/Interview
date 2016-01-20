# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:43:03 2015

@author: zeevandeep
"""

def powersetlist(s):
    r = [[]]
    for e in s:
        #print "r: %-55r e: %r" % (r,e)
        r += [x+[e] for x in r]
    return r
 
s= [0,1,2,3]    

#print "\npowersetlist(%r) =\n  %r" % (s, powersetlist(s))

def power(set1):
    powerset =[[]]
    for n in set1:
        newpowerset = []
        for m in powerset:
            newpowerset.append(m+[n])
            newpowerset.append(m)
        powerset = newpowerset

    return powerset  



set1= [1,2,3]
print "\npowersetlist(%r) =\n  %r" % (set1, power(set1))
