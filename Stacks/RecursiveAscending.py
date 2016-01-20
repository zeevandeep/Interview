class Stack:
	def __init__(self):
		self.stk=[]
	
	def push(self,data):
		self.stk.append(data)

	def peek(self):
		return self.stk[-1]
	
	def pop(self):
		return self.Stack.pop()

	def isEmpty(self):
		return len(self.stk) == 0


def sort(stack1,stack2):
	temp = stack1.pop()

	while not stack1.isEmpty():
		if stack1.peek() >= temp:
			stack2.push(stack1.pop())
		else:
			stack2.push(temp)
			temp = stack1.pop()
	








s= Stack()
s.push(32)
s.push(4)
s.push(51)
s.push(12)
s.push(13)


sort(s, Stack())