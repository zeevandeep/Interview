sentence = 'My name is Jeevandeep and you know I am a friend of Soura'

iteration=len(sentence)/16
remainder=len(sentence)%16
start=0
end=15
if remainder!=0:
	iteration=iteration+1

for x in range(iteration):
	
	if sentence[end]!=' ':
		while sentence[end]!=' ':
			end=end-1
		

	
			
	print sentence[start:end]
	start=end+1
	end=start+15

	
	if end >= len(sentence):
		print sentence[start:]
		break



