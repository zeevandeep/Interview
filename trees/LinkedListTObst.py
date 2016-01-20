#Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
class BSTnode():
	def __init__(self, data):
		
		self.root  = None
		self.right = None
		self.left  = None
		self.data = data
	
	def setRight(self,node):
		self.right = node

	def setleft(self,node):
		self.left = node

	def getRight(self):
		return self.right

	def getleft(self):
		return self.left

	def getdata(self):
		return self.data
	def __repr__(self):
		return self.data

	

class Bstree
	def insert(self,linkedlist):
		for i in linkedlist:
			head = linkedlist[i]
			newnode = BSTnode(head)
			self.root = node
			if self.root == None:
				self.root = newnode
				break
			else:
				node = self.root
			while node != None:
				if node.getdata() < linkedlist[i]:
					if not node.getRight():
						node.setRight(newnode)
					else:
						node=node.getRight()

				else:
					if not node.getleft():
						node.setleft(newnode)
					else:
						node = node.getleft()
	def BalancedheightTree(self):
		





