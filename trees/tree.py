class binaryTree():
	def __init__(self,data):
		self.value=data
		self.left=None
		self.right=None
		self.parent=None

	
	def getValue(self):
		return self.value
	
	def setLeftBranch(self,node):		
		self.left=node

	def setRightBranch(self,node):
		self.right = node
	
	def getRightBranch(self):
		return self.right
	
	def getLeftBranch(self):
	 	return self.left


	def setParent(self,parent):
		self.parent=parent
	
	def getParent(self):
		return self.parent

	def __str__(self):
		return (self.value)

	def Tracepath(self,node):
		if not node.getParent():
			return [node]
		else:
			return [node] + self.Tracepath(node.getParent())


	def DFS(self,root,value):
		stk=[root]
		print stk[0].getValue()
		while len(stk)>=1:
			print "At Node" + str(stk[0].getValue())
			if (value == stk[0].getValue()):
				return self.Tracepath(stk[0])
			else:
				tmp = stk.pop(0)
				if tmp.getRightBranch():
					stk.insert(0,tmp.getRightBranch())
				if tmp.getLeftBranch():
					stk.insert(0,tmp.getLeftBranch())

	def BFS(self,root,value):
		queue=[root]
		#print stk[0].getValue()
		while len(queue)>=1:
			print "At Node" + str(queue[0].getValue())
			if (value == queue[0].getValue()):
				print "Found"
				#print stk[0].getValue()
				break
			else:
				tmp = queue.pop(0)
				if tmp.getRightBranch():
					queue.append(tmp.getLeftBranch())
				if tmp.getLeftBranch():
					queue.append(tmp.getRightBranch())

	def inorder(self,node):
		if not node:
			return
		else:
			self.inorder(node.getLeftBranch())
			print node.getValue()
			self.inorder(node.getRightBranch())

	def  postorder(self,node):
		if not node:
			return
		else:
			self.postorder(node.getLeftBranch())
			self.postorder(node.getRightBranch())
			print node.getValue()

	def  preorder(self,node):
		if not node:
			return
		else:
			print node.getValue()
			self.preorder(node.getLeftBranch())
			self.preorder(node.getRightBranch())

	def printTree(self,node):
		level =0
		current =[(level,node)]
		while current:
			l,n= current.pop(0)
			print n.getValue(),

			if n.getLeftBranch:
				current.append((level+1,n.getLeftBranch()))
			if n.getRightBranch:
				current.append((level+1,n.getRightBranch()))

			if current and current[0][0]!=l:
				level+=1
				print ""

	def sumToLeafNodes(self,node,presum): # Not working here but working in LeetCode
		if not node:
			return 0
		else:
			presum=presum*10 + node.getValue()
			if not node.getLeftBranch() and not node.getRightBranch():
				return presum
			return self.sumToLeafNodes(node.getValue(),presum) + self.sumToLeafNodes(node.getRightBranch(),presum)

	def sumToLeafHelper(self,node):
		return self.sumToLeafNodes(node,0)



			


n5 = binaryTree(2)
n2 = binaryTree(3)
n1 = binaryTree(1)
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)
n3 = binaryTree(3)
k1=binaryTree(1)
k2=binaryTree(2)
k3=binaryTree(3)
k4=binaryTree(4)
k5=binaryTree(5)
k6=binaryTree(6)
k7=binaryTree(7)
k8=binaryTree(8)
k1.setLeftBranch(k2)
k1.setRightBranch(k3)
k2.setRightBranch(k5)
k2.setLeftBranch(k4)
k3.setLeftBranch(k6)
k3.setRightBranch(k7)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
n4.setLeftBranch(n3)
n3.setParent(n4)
#print n5.inorder(n5)
#n5.DFS(n5,6)
#print n5.printTree(n5)
##print 'DFS path'
#pathTo6 = n5.DFS(n5, 6)
#print [e.getValue() for e in pathTo6]

print n5.sumToLeafHelper(k1)


