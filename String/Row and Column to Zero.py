def convertRowColumntoZero(matrix):
	import copy
	new_mat=copy.deepcopy(matrix)
	size = len(matrix)
	for i in range(size):
		for j in range(size):
			if matrix[i][j]== 0:
				for k in range(size):
					for l in range(size):
						new_mat[i][l]=0
						new_mat[k][j]=0
	[print (p) for p in new_mat]

if __name__ == '__main__':
	matrix=[[1,2,3,0],[5,6,7,8],[1,10,11,12],[13,14,15,16]]
	convertRowColumntoZero(matrix)