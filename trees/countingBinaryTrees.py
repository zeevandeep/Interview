T=[5]
T[0]=1
T[1]=1
n=5
for i in range(2,n):
	for j in range(0,i):
		T[i].append(T[j] * T[i-j-1])
for k in T:
	print k 