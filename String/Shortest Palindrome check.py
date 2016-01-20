#aacecaaa", return "aaacecaaa".

#Given "abcd", return "dcbabcd".


def palinderome(s):
	tmp = (s+'x')[:-1]
	finalcheck=''
	check = ''
	palinderome =False

	while not palinderome:
		last = tmp[-1]
		check+=last

		finalcheck = check + s
	   	reverse = finalcheck[::-1]
	   	if finalcheck == reverse:
	   		palinderome = True
	   		return finalcheck
	   		break
	   	else:
	   		tmp=tmp[:-1]
	   		finalcheck=''

print palinderome('aacecaaa')