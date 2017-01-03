# Given an array, find the next greater element G[i] for every element A[i] in the array. 
# The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. 
def Solve_BF(A):
	if len(A) < 1:
		return A
	if len(A) == 1:
		return [-1]
	result = []
	for i in range(len(A)):
		flag = False
		for j in range(i+1,len(A)):
			if A[j] > A[i]:
				result.append(A[j])
				flag = True
				break
		if flag == False:
			result.append(-1)
	return result
def Solve_Stack(A):
	if len(A) < 1:
		return A
	if len(A) == 1:
		return [-1]
	stack = []
	myDict = dict()
	result = []
	for i in range(len(A)):
		while stack and A[stack[-1]] < A[i]:
			myDict[stack[-1]] = A[i]
			stack.pop()
		stack.append(i)
	while stack:
		myDict[stack[-1]] = -1
		stack.pop()
	for i in range(len(A)):
		result.append(myDict[i])
	return result
# A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
# A = [ 7, 6, 5, 4, 3, 2, 1 ]
A = [ 39, 27, 11, 4, 24, 32, 32, 1 ]
print A
print Solve_BF(A)
print Solve_Stack(A)
