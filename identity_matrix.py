def is_identity_matrix(matrix):
	if matrix==[]:
		return True
	if len(matrix)!=len(matrix[0]):
		return False
	size=len(matrix)
	horizontalindex=0
	while horizontalindex<=size-1:
		verticalindex=0
		while verticalindex<=size-1:
			if horizontalindex==verticalindex:
				if matrix[horizontalindex][verticalindex]==1:
					verticalindex=verticalindex+1
					if verticalindex>size-1:
						break
				else:
					return False
			if horizontalindex!=verticalindex:
				if matrix[horizontalindex][verticalindex]==0:
					verticalindex=verticalindex+1
					if verticalindex>size-1:
						break
				else:
					return False
		horizontalindex=horizontalindex+1
	return True