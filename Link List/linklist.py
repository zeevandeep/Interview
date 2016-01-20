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

	def __str__(self):
		return str(self.data)
	
	
	
class list:
	def __init__(self):
		self.head=None
		self.length=0

	def setHead(self, head):
		self.head=head

	def setLength(self, length):
		self.length=length

	def insert(self,data):
		newNode=Node()
		newNode.setData(data)


		if self.length > 0:
			newNode.setNext(self.head)
		self.head = newNode

		self.length+=1

	"""def print_list(newNode):
    	while newNode:
        	print newNode,
        	newNode = newNode.next
    	print"""
	
	def __str__(self):
		if self.length==0:
			return "empty"
		else:
			l = ""
			current=self.head
			
			while current.getNext()!=None:
				l+=str(current.getData()) + "-->"
				current = current.getNext()
			l+=str(current.getData())
			return l	

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

	def search(self,data):
		current=self.head
		while current!=None:
			if current.data == data:
				return True
			current=current.getNext()
		return False
	
	def deleteAtpos(self,pos):
		current=self.head
		previous=self.head
		count=1
		while count < pos-1:
			current=current.getNext()
			previous=previous.getNext()
			count+=1
		current=current.getNext()
		previous.setNext(current.getNext())
		return pos
		
	
	def deleteAtend(self):
		current=self.head
		previous=self.head
		while current.getNext()!=None:
			previous = current
			current=current.getNext()
		previous.setNext(None)
		return
	

	def Palindrome(self):
		current=self.head
		last=self.head
		b=0
		if last!=None:
			self.Palindrome(last.getNext())
		if current.getData() == last.getData():
			current=current.getNext()
			b=0
		else:
			b=1

    
	def newDeleteCode(self,pos):
		

		current = self.head
		previous = self.head
		count =1
		if pos is 1:
			self.head = self.head.getNext()
		else:

			while count<  pos:
				previous = current
				current = current.getNext()
				count+=1
			previous.setNext(current.getNext())
			return pos

	def newRemoveDuplicate(self):
		original =self.head
		
		while original!=None:
			current = original.getNext()
			previous = original
			while current!= None:
				if current.getData() == original.getData():
					if current.getNext() == None:
						previous.setNext(None)
					previous.setNext(current.getNext())
					current = current.getNext()
				else:
					current = current.getNext()
					previous = previous.getNext()
			print "Tree is ",self
			original=original.getNext()

    

	def newreverse(self):
		current =  self.head.getNext()
		previous = self.head
		rcurrent = current.getNext()
		previous.setNext(None)
		while current != None:
			
			current.setNext(previous)
			previous = current
			current = rcurrent
			if rcurrent:
				rcurrent=rcurrent.getNext()
		self.head = previous
		

	def deleteAlternateLinkedList(self):
		current  = self.head.getNext()
		previous = self.head
		while current != None:
			previous.setNext(current.getNext())
			current = previous.getNext()
			if current == None:
				pass
			else:
				current  = current.getNext()
				previous = previous.getNext()


	def recursiveReverseHelper(self):
		return self.recursiverReverseImp(self.head)

	def recursiverReverseImp(self,node):
		if node is not None:
			current = node.getNext()
			if node != self.head:
				node.setNext(self.head)
				self.head = node
			else:
				node.setNext(None)

			self.recursiverReverseImp(current)

	def recursiveReverse2(self):
		self.setHead(self.recursiveReverse2Impl(self.head, None))

	def recursiveReverse2Impl(self, head1, head2):
		if head1:
			t = head1
			head1 = head1.getNext()
			t.setNext(head2)
			head2 = t
			return self.recursiveReverse2Impl(head1, head2)
		else:
			return head2

	def reverse(self):
		current = self.head
		currentnext = self.head
		future = current.next

		while currentnext!= None:
			
			if future.next!= None:
				future=future.next

			currentnext.next=current
			current=currentnext
		current=self.head

if __name__ == "__main__":
	m=list()
	m.insertLast(1)
	m.insertLast(2)
	m.insertLast(3)
	m.insertLast(4)
	m.insertLast(4)
	m.insertLast(3)
	m.insertLast(2)
	
	

	print m
	
	m.reverse()

	print m
	#m.recursiveReverseHelper()
	#print m
	#m.recursiveReverse2()
	#print m
    
	#print m.Palindrome()
	







