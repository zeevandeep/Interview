def reverseStringRecursive(str1):
    if str1 != "":
    	return str1[-1:] + reverseStringRecursive(str1[:-1])
    else:
       	return ""
reverseStringRecursive('hello')
