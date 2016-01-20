class TreeNode:
	def __init__(self,data):
		self.data  = data
		self.right = None
		self.left  = None
		

	def __repr__(self):
		return str(self.data)

class Tree:
	def __init__(self):
		self.root = None
		self.arr = []
		self.arr1 = []
		self.arr2 =[]
	def insert(self,data):
		newNode = TreeNode(data)
		if not self.root:
			self.root = newNode
			return
		else:
			node = self.root

			while node:	
				if data < node.data:
					if not node.left:
						node.left = newNode
						return
					node = node.left

				if data > node.data:
					if not node.right:
						node.right = newNode
						return
					node = node.right

	def printTree(self):
		node = self.root 
		level =0
		current = [(level,node)]
		while current:
			l,n = current.pop(0)
			print n.data,
			if n.left:
				current.append((level+1,n.left))
			if n.right:
				current.append((level+1,n.right))
			
			if current and current[0][0] !=l:
				level=level+1
			 	print
		
	def array(self,arr,node):
		if not node:
			return
		else:
			self.array(self.arr,node.left)
			self.arr.append(node.data)
			#print node.data
			self.array(self.arr,node.right)



	def dividetree(self,data):
		stk     = [self.root]
		current = stk.pop(0)
		arr = []
		if current.data == data:
			arr1 = self.array(arr,current)
			return arr1
		else:
			if current.right:
				stk.insert(0,current.right)
			if current.left:
				stk.insert(0,current.left)
		return arr
	

	def checksubtree(self):
		arr=[None]
		arr2 = self.array(arr,self.root)
		print self.arr1
		print self.arr2
		if self.arr1 ==self.arr2:
			return True
		else:
			return False



tree = Tree()
c = tree.insert(50)
tree.insert(25)

tree.insert(12)
tree.insert(28)
tree.insert(80)
tree.insert(52)
tree.insert(45)
tree.insert(100)
tree.insert(34)
#tree.printTree()
tree.dividetree(28)
a= Tree()
a.insert(12)
a.insert(45)
a.insert(34)

#a.printTree()
print a.checksubtree()


















