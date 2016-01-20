a='iceman '
n='cinema'
if len(a)!= len(n):
	print (False)
c=0
b=0
for i in a:
	c+=ord(i)
	
for g in a:
	b+=ord(g)
if c==b:
	print (True)
else:
	print (False)