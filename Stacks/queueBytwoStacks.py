class queue:
	def __init__(self):
		self.stk1=[]
		self.stk2=[]
	def push(self,data):
		self.stk1.append(data)
		self.stk2=self.stk1[::-1]
	def pop(self):
		if len (self.stk2) < 1:
			print ("Stack is empty")
		else:
			x = self.stk2.pop()
			self.stk1.remove(x)

		print("The popped item is ", x)
	def __str__(self):
		return str(self.stk1)



q = queue()
q.push(5)
q.push(6)
q.push(7)
q.push(8)
q.pop()
print (q)
