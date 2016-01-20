class Stack:
	def peak(self):
		return self[-1]
	def push(self, item):
		self.append(item)
	def empty(self):
		return len(self) == 0

	def sort_stack(self):
		r = Stack()
		while not self.empty():			
			tmp = self.pop()
			while not r.empty() and r.peak() > tmp:
				self.push(r.pop())
			r.push(tmp)
			while not self.empty() and self.peak() >= r.peak():
				#warning, >= here
				r.push(self.pop())
		print (r)
s = Stack(3,1,0,4,2)
s.sort_stack()