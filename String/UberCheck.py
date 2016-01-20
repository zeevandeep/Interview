sentence = 'My name is Jeevandeep and you know I am a friend of Soura'
position=0
start=0
end=0
for i in range(len(sentence)):
	start=start+1
	end=end+1

	if(start%16==0 and start!=0):

		if (sentence[end]!=' '):
			while sentence[end]!=' ':
				end=end-1
			start=0
			
		
		print sentence[position:end]

		position=end+1
		end=position+start
	

print sentence[position:]
