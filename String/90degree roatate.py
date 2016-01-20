def rotate(matrix):
	import copy
	
	new=copy.deepcopy(matrix)
	#[print(i) for i in mat]
	size= len(matrix)
	for i in reversed(range(size)):
		for j in range(size):
			#print (mat[i][j])
			new[j][size-1-i]=matrix[i][j]
	[print (k) for k in new]

if __name__ == '__main__':

	matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	rotate(matrix)