class setOfStacks:
	def __init__(self,capacity):
		capacity=100
		self.stk=[]
	def push(self,data):
		noOfStacks=capacity/100
		if noOfStacks%100: 
			noOfStacks+=1
		for initialize in range