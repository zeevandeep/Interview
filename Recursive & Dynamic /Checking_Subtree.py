class node:
	def __init__(self,data,left,right):
		self.data=data
		self.left=left
		self.right=right

	def __str__(self):
		return self.data

	def __repr__(self):
		return self. __str__()

class Tree:
	def __init__(self,root):
		self.root=root

	def isSubTree(self, tree2):
		nodes = [self.root]
		while nodes:
			node = nodes.pop()
			if (node.data == tree2.root.data):
				if (self.areEqual(node, tree2.root)):
					return True
			if (node.left):
				nodes.append(node.left)
			if (node.right):
				nodes.append(node.right)

		return False

	def areEqual(self, node1, node2):
		if (not node1) and (not node2):
			return True
		if node1 and not node2:
			return False
		if node2 and not node1:
			return False

		return node1.data == node2.data and \
			self.areEqual(node1.left, node2.left) and \
			self.areEqual(node1.right, node2.right)

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

k11=node(85,None,None)
k12=node(95,None,None)   
k1=node(90,k11,k12)

binary=Tree(n1)
print binary.isSubTree(Tree(k1))




