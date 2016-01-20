class binaryTree:
	def __init__(self,data):
		self.data  = data
		self.right = None
		self.left  = None

	def common(self,root,data1,data2):
		stk=[root]
		stk1=[root]
		Found = False
		Found1 = False
		arr =[]
		arr1 = []
		while not Found and stk:
			if data1==root.data:
				Found = True
				break
			else:
				current = stk.pop(0)
				arr.append(current.data)
				if data1 < current.data and current.left:
					stk.insert(0,current.left)
				else:

					if data1 > current.data and current.right:
						stk.insert(0,current.right)
				
		while not Found1 and stk1:

			if data2==root.data:
				Found = True
				break
			else:
				current = stk1.pop(0)
				arr1.append(current.data)
				if data2 < current.data and current.left:
					stk1.insert(0,current.left)

				else:

					if data2 > current.data and current.right:
						stk1.insert(0,current.right)
		print arr 
		print arr1
		for i in range(min(len(arr),len(arr1))):
			if arr[i] == arr1[i]:
				continue
			else:
				return arr[i-1]

		return "Not Found"


n5 = binaryTree(2)
n2 = binaryTree(7)
n1 = binaryTree(5)
n4 = binaryTree(2)
n8 = binaryTree(6)
n6 = binaryTree(5)
n7 = binaryTree(11)
n3 = binaryTree(9)
n10= binaryTree(4)

n5.left =n2
n5.right = n1
n1.right = n3
n3.left = n10
n2.left = n4
n2.right = n8
n8.left = n6
n8.right = n7

print n5.common(n5,5,11)



		