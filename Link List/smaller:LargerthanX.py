class Node:
	def __init__(self):
		self.data=None
		self.next=None
	
	def setData(self,data):
		self.data=data
	
	def getData(self):

		return self.data
	
	def setNext(self,next):
		self.next=next
	
	def getNext(self):
		return self.next
	
	def hasNext(self):
		return self.next!=None

class list:
	def __init__(self):
		self.head=None
		self.length=0

	def insert(self,data):
		newNode=Node()
		newNode.setData(data)


		if self.length > 0:
			newNode.setNext(self.head)
		self.head = newNode

		self.length=self.length+1

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

	def Found(self,value):
		current=self.head
		Found=False
		while not Found:
			if current.getData()==value:
				Found=True
				previous=current
			current=current.getNext()
		if Found==True:
			previous=self.head
			if previous.get


	
	def Partition(self):

		if self.Found()==True:
			 




