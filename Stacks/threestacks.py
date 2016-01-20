class ThreeStacks:
	def __init__(self, maxSize):
		self.list = [None] * maxSize
		self.top1 = -1
		self.size = maxSize / 3
		self.top2 = self.size-1
		self.top3 = self.size*2-1
		


	def push(self, stackNo, data):
		#print self.top1,self.top2,self.top3
		
		if self.top1==self.size and self.top2 == self.size*2 and self.top3==self.size*3:
			print "Stack is Full"
			
		elif stackNo == 0:

			self.top1 = self.top1 + 1
			if self.top1==self.size:
				return "Stack One is Full"
				
			self.list[self.top1] = data
			

		elif  stackNo == 1:
		 	self.top2 = self.top2+1
		 	if self.top2==self.size*2:
				return "Stack Two is Full"
		 	self.list[self.top2]=data
		 	

		elif  stackNo == 2:
			self.top3 = self.top3+1
		 	if self.top3==self.size*3:
				return "Stack Three is Full"
		 	self.list[self.top3]=data
		 

		
		return self.list
	
	def pop(self,stackNo):
		if stackNo==0:
			if self.top1==-1:
				print "Stack is Empty"
				return

			delete = self.list[self.top1]
			self.list[self.top1]=None

			self.top1-=1
		if stackNo==1:
			
			if self.top2==self.size-1:
				print "Stack is Empty"
				return

			delete = self.list[self.top2]
			self.list[self.top2]=None

			self.top2-=1
			

		if stackNo==2:

			if self.top3==self.size*2-1:
				print "Stack is Empty"
				return

			delete = self.list[self.top3]
			self.list[self.top3]=None

			self.top3-=1
			

		return delete

	def __str__(self):
		return str(self.list)

a=ThreeStacks(9)
a.push(0,10)

a.push(0,23)
a.push(0,89)

a.push(2,6)
a.push(2,9)
a.push(2,10)
a.push(2,45)
a.pop(0)
a.pop(0)


print a













