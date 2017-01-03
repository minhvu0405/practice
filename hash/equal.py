# Given an array A of integers, find the index of values that satisfy A + B = C + D,
# where A,B,C & D are integers values in the array
# Return the indices `A1 B1 C1 D1`, so that 
#   A[A1] + A[B1] = A[C1] + A[D1]
#   A1 < B1, C1 < D1
# 	A1 < C1, B1 != D1, B1 != C1 
# If there are more than one solutions, 
#    then return the tuple of values which are lexicographical smallest. 
def Solve(A):
	Dict = {}
	result = []
	for i in range(len(A)-1):
		for j in range(i+1,len(A)):
			m = A[i] + A[j]
			if m not in Dict:
				Dict[m] = [i,j]
			else:
				if Dict[m][0] == i or Dict[m][1] == j or Dict[m][0] == j or Dict[m][1] == i:
					continue
				result.append(Dict[m] + [i,j])
	# return sorted(result)[0] if result else []
	# implement sorted(result)[0]
	for i in range(4):
		smallest = float('inf')
		temp = []
		for j in range(len(result)):
			if result[j][i] < smallest:
				smallest = result[j][i]
		for j in range(len(result)):
			if result[j][i] == smallest:
				temp.append(result[j])
		result = temp
		if len(result) == 1:
			return result[0]
	if result:
		return result[0] 
	return []
A = [3, 4, 7, 1, 2, 9, 8]
print Solve(A)
