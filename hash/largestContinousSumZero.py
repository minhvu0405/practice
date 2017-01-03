# Find the largest continuous sequence in a array which sums to zero.
def Solve_BF(A):
	if len(A) < 1:
		return A
	biggest = -float('inf')
	result = None
	for i in range(len(A)):
		s = 0
		for j in range(i,len(A)):
			s += A[j]
			if s == 0 and j-i+1 > biggest:
				biggest = j-i+1
				result = i,j+1
	if result:
		return A[result[0]:result[1]]
	return None
def Solve_Hash(A):
	if len(A) < 1:
		return A
	maxLength = -float('inf')
	myDict = dict()
	s = 0
	for i in range(len(A)):
		s += A[i]
		if A[i] == 0 and maxLength == 0:
			maxLength = 1
		if s == 0:
			maxLength = i + 1
			index = i
		if s in myDict:
			n = i - myDict[s]
			if n > maxLength:
				maxLength = n
				index = i
		else:
			myDict[s] = i
	if maxLength:
		return A[index-maxLength+1:index+1]
	return
t = [1 ,2 ,-2 ,4 ,-4]
t1 = [ 1, 2, -3, 3 ]
t2 = [1 ,2 ,-2 ,4 ,-2,-1,1]
# print Solve_BF(t2)
print Solve_Hash(t2)