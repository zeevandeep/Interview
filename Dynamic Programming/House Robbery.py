num=[50,30,100,200,20,]
total0,total1 = 0,0
for item in num:
	total0,total1 = max(total0,total1), total0+item 
print max(total1,total0)