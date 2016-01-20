# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Node():
    def __init__(self,data,next):
        self.data= data
        self.next= next

class BSTTreeNode():
    def __init__(self,data,right,left):
        self.data = data
        self.right = right
        self.left = left

class Linklist():
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def insert(self, data):
        newNode = Node(data,None)
        if self.length ==0:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
        self.length+=1
    
    def __str__(self):
        if self.length == 0:
            return
        else:
            k=''
            node= self.head
            while node.next != None:
                k+=str(node.data) + "-->"
                node = node.next
            k+=str(node.data)
        return k
        
class Tree():
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        newNode = BSTTreeNode(data,None,None)
        if not self.root:
            self.root = newNode
        else:
            node = self.root
            if data < node.data:
                if not node.left:
                    node.left = newNode
                    return
                node = node.left
            elif data > node.data:
                if not node.right:
                    node.right = newNode
                    return
                node = node.right
   
                
        
    def depth(self):
        level = 0
        node = self.root
        queue = [(level,node)]
        lists =[]        
        
        while queue:
            print queue
            l, n = queue.pop(0)
            if len(lists) == l:
                lists.append(Linklist())
            print l,level
            lists[l].insert(n.data)
            if n.left:
                queue.append((level+1,n.left))
            if n.right:
                queue.append((level+1,n.right))
            
            if queue and queue[0][0] != l:
                level+=1
            
        for i in lists:
            print i
                
            
t= Tree()
t.insert(40)
t.insert(30)
t.insert(50)
t.insert(20)
t.insert(65)
t.insert(75)
t.depth()


     