# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:11:02 2015

@author: zeevandeep
"""


class node:

    def __init__(self, data, left, right):
        self.data = data
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.data)
        
    def __repr__(self):
        return self.__str__()


class Tree:

    def __init__(self, root):
        self.root = root

    def printTree(self):
        node = self.root
        level = 0
        current = [(level, node)]
        while current:
            l, n = current.pop(0)
            print n,
            if n.left:
                current.append((level + 1, n.left))
            if n.right:
                current.append((level + 1, n.right))
            
            #print current

            if current and current[0][0] != l:
                level = level + 1
                print


    def isBst(self):
        return self.isBstImpl(self.root)
        
    def isBstImpl(self, node):

        if node.left and not self.isBstImpl(node.left):
            return -1
        if node.right and not self.isBstImpl(node.right):
            return -1 

            
        if(node.left==None and node.right==None):
            return 1
            
        if(node.left and node.left.data > node.data):
            return -1
        
        if(node.right and node.right.data < node.data):
            return -1
            
        return 1




n7=node(20,None,None)
n8=node(35,None,None)
n9=node(60,None,None)
n10=node(75,None,None)
n11=node(85,None,None)
n12=node(95,None,None)                  

n4=node(30,n7,n8)
n5=node(70,n9,n10)
n6=node(90,n11,n12)

n2=node(40,n4,None)
n3=node(80,n5,n6)

n1=node(50,n2,n3)

binary=Tree(n1)
binary.printTree()
print binary.isBst()




      
    
        
