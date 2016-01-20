
class BSTreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def setLeft(self, node):
		self.left = node

	def setRight(self, node):
		self.right = node

	def getData(self):
		return self.data

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setData(self,data):
		self.data=data

	def setparent(self,node):
		self.parent=node

	def getparent(self):
		return self.parent

	def __repr__(self):
		return str(self.data)


class BSTree:
	def __init__(self):
		self.root = None


	def insert(self, data):
		newNode = BSTreeNode(data)

		if not self.root:
			self.root = newNode
			newNode.setparent(None)
		else:
			node = self.root

			while node != None:
				if data > node.getData():
					if node.getRight() == None:
						node.setRight(newNode)
						newNode.setparent(node)
						return
					node = node.getRight()

				elif data < node.getData(): 
					if node.getLeft() == None:
						node.setLeft(newNode)
						newNode.setparent(node)
						return
					node = node.getLeft()

	def height(self):
		return self.heightImpl(self.root)

	def heightImpl(self,node):
		if not node:
			return 0
		else:
			return max(self.heightImpl(node.getLeft()),self.heightImpl(node.getRight())) +1

	def printTree(self):
		node = self.root
		level = 0
		current = [(level,node)]
		while current:
			l, n = current.pop(0)
			print n.getData(),
			if n.getLeft():
				current.append((level+1, n.getLeft()))
			if n.getRight():
				current.append((level+1, n.getRight()))
			
			#print current
			if current and current[0][0] != l:
				level = level + 1
				print

	def delete(self,data):
		return self.deleteImpl(self.root, data)

	def findtobedeleted(self,data):
		parent = None
		leftchild = None
		node = self.root
		
		while node:
			if node.getData() == data:
				return node,leftchild, parent

			elif node.getData() > data:
				parent=node
				node=node.getLeft()
				leftchild = True

			else:
				parent=node
				node=node.getRight()
				leftchild =False

		raise Error()

	def deleteImpl(self,node,data):
		node1, leftchild,parent = self.findtobedeleted(data)
		print("From find node to delete: ", node1, leftchild, parent)
		
		if(node1.getRight()==None and node1.getLeft()==None):
			if leftchild ==True:
				parent.setLeft(None)
			else:
				parent.setRight(None)

		elif node1.getRight() and not node1.getLeft():
			if leftchild == False:
				parent.setRight(node.getRight())
			else:
				parent.setLeft(node.getRight())

		elif node1.getLeft() and not node1.getRight():
			if leftchild ==False:
				parent.setRight(node.getLeft())
			else:
				parent.setLeft(node.getLeft())
		else:
			node2, parent2 = self.Minimunintree(node1.getRight(),node1) 
			print (" Minimunintree Node and Parent",node2,parent2)
			if parent2 == node1:
				parent2.setRight(None)
			else:
				parent2.setLeft(None)
			node1.setData(node2.getData())

	def Minimunintree(self,node,parent):
		while node.getLeft()!=None:
			parent = node
			node=node.getLeft()
		return  node,parent

	def Recursive(self,data):
		return self.RecursiveSearch(self.root,data)
	
	
	def RecursiveSearch(self,node,data):
		if not node:
			return None
		elif(data < node.getData()):
			self.RecursiveSearch(node.getLeft(),data)
		elif(data > node.getData()):
			self.RecursiveSearch(node.getRight(),data)
		else:
			print node.getData()

	
	def LowestAncestor(self,n1,n2):
		node = self.root
		while node:
			if node.getData() > n1 and node.getData() > n2:
				node=node.getLeft()
			elif node.getData() < n1 and node.getData() <n2:
				node= node.getRight()
			else:
				break
		return node				

	def BalancedTree(self):
		node=self.root
		return self.BalancedTreeImpl(node)



	def BalancedTreeImpl(self,node):
		if node:
			leftHeight  = self.heightImpl(node.getLeft())
			rightHeight = self.heightImpl(node.getRight())

			if abs(leftHeight - rightHeight) > 1 :
				return False
			else:
				return self.BalancedTreeImpl(node.getLeft()) and self.BalancedTreeImpl(node.getRight())
		else:		
			return True
	
	def MinimalHeightOfSortedArray(self,array):
		if len(array) == 0:
			return 
		else:
			mid = len(array)/2
			self.insert(array[mid])
			self.MinimalHeightOfSortedArray(array[0:mid])
			self.MinimalHeightOfSortedArray(array[mid+1:])

	def mindepth(self):
		return self.mindepthImp(self.root)

	def mindepthImp(self,node):
		if node.getLeft() == None or node.getRight() == None:
			return 0
		else:
			return min(self.mindepth(node.getLeft()),self.mindepth(node.getRight())) + 1

	def Immediatesuccesor(self,node):
		return [node.getparent()]

	def array(self,arr,node):
		if not node:
			return
		else:
			self.array(self.arr,node.getleft())
			self.arr.append(node.getdata())
			self.array(self.arr,node.getright())

	def binaryImpl(self,node,mini,maxi):
		if not node:
			return True
		if node.getData() > mini and node.getData() < maxi and self.binaryImpl(node.getLeft(),mini,node.getData()) and self.binaryImpl(node.getRight(),node.getData(),maxi):
			return True
		else:
			return False

	def binary(self):
		mini =float("inf")
		maxi = float("-inf")

		return self.binaryImpl(self.root,mini,maxi)



tree = BSTree()
#array=[10,20,30,40,50,60,70]
#tree.MinimalHeightOfSortedArray(array)
#print tree
a =tree.insert(100)
tree.insert(50)

tree.insert(40)
tree.insert(60)
tree.insert(150)
tree.insert(130)
c = tree.insert(190)
#tree.insert(95)
#tree.insert(7)
#tree.insert(13)
tree.delete(100)
#print tree 
print ''

tree.printTree()
#print tree.BalancedTree()
print ''
print ''

#tree.mindepth()
#tree.printTree()
#print tree.array([],a)
#print tree.Immediatesuccesor()


