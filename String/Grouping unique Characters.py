string="aaabbbca"
group=[]
previous_character=string[0]
counter=1
for current_char in string[1:]:

	if current_char==previous_character:
		counter+=1
	else:
		group.append(previous_character + str(counter) )
		counter=1
		previous_character=current_char
group.append(previous_character+str(counter))
result = ''.join(group)
print (result) 
