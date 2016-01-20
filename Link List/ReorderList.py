class Node:
	def __init__(self,data,next):
		self.data=data
		self.next=next

class linkedlist:
	def __init__(self):
		self.head=None

	def insert(self,data):
		newNode = Node(data,None)
		if self.head:
			current=self.head
			while current.next != None:
				current=current.next
			current.next=newNode
		else:
			self.head=newNode

	def __str__(self):
		if not self.head:
			return "empty"
		else:
			l = ""
			current=self.head
			
			while current.next!=None:
				l+=str(current.data) + "-->"
				current = current.next
			l+=str(current.data)
			return l	

	def reverse(self, head):
		last = None
		current = head

		while current:
			nxt = current.next
			current.next = last 
			last = current
			current = nxt
		
		return last
		

	def reorder(self):
		fast = self.head
		slow = self.head
		while(fast!= None and fast.next!=None and fast.next.next!=None):
			slow=slow.next
			fast=fast.next.next

		secondhead = slow.next
		slow.next = None
		
		print self

		first=self.head
		second = self.reverse(secondhead)
		while (first and second):
			temp1 = first.next
			temp2 = second.next
			first.next = second
			second.next  = temp1
			first = temp1
			second  = temp2


if __name__ == "__main__":
	m=linkedlist()
	m.insert(1)
	m.insert(2)
	m.insert(3)
	m.insert(4)
	m.insert(6)
	m.insert(7)
	m.insert(8)

	print m
	m.reorder()
	print m

