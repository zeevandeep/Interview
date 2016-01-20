from linklist import Node
# class Node:
# 	def __init__(self):
# 		self.data=None
# 		self.next=None
	
# 	def setData(self,data):
# 		self.data=data
	
# 	def getData(self):

# 		return self.data
	
# 	def setNext(self,next):
# 		self.next=next
	
# 	def getNext(self):
# 		return self.next
	
# 	def hasNext(self):
# 		return self.next!=None

class Element:
	def __init__(self):
		self.head=None
		self.length=0

	def insertLast(self,data):
		newNode=Node()
		newNode.setData(data)

		if self.length==0:
			self.head=newNode
		else:
			current=self.head
			while current.getNext()!=None:
				current=current.getNext()
			current.setNext(newNode)
		self.length+=1

	def getKtoLastElements(self,pos):
		count=0
		current=self.head
		l=""
		while count < pos-1:
			current=current.getNext()
			count+=1

		while current != None:
			l+=str(current.data)+"-->"

			current=current.getNext()
		return l
		


	def __str__(self):
		if self.length==0:
			return "empty"
		else:
			l = ""
			current=self.head
			
			while current!=None:
				l+=str(current.getData()) + "-->"
				current = current.getNext()
			return l	

m=Element()
m.insertLast(1)
m.insertLast(2)
m.insertLast(3)
m.insertLast(4)
m.insertLast(2)
m.insertLast(4)
m.insertLast(1)
m.insertLast(2)
print m
print m.getKtoLastElements(3)











		