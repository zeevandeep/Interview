class Stack:
	def __init__(self):
		self.stk=[]
		self.ascStk=[]
	
	def push(self,data):
		self.stk.append(data)

	def peek(self):
		return self.stk[-1]
	
	def sort(self):
	
		if len (self.ascStk) < 1:
			tmp = self.stk.pop()
		else:
			tmp = self.ascStk.pop()

		while len(self.stk) < 1 or len(self.ascStk) < 1:
			if len (self.ascStk)< 1:
				k = self.stk.pop()
				if k < tmp:
					self.ascStk.push(tmp)
					tmp=k
				else:
					self.ascStk.append(k)
		return self.stk.push(tmp) + self.sort()










s= Stack()
s.push(32)
s.push(4)
s.push(51)
s.push(12)
s.push(13)


s.sort()