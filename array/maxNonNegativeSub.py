def maxNonNegSub(A):
	if len(A) == 0:
		return 
	allneg = True
	subSum = finalSum = 0
	firstIndex = endfirstIndex = 0
	first = 0
	for i in range(len(A)):
		if A[i] >= 0:
			allneg = False
			subSum += A[i]
		else:
			subSum = 0
			first = i+1
		if finalSum < subSum:
			finalSum = subSum
			firstIndex = first
			endfirstIndex = i
		elif finalSum == subSum:
			if endfirstIndex + 1 - firstIndex < i + 1 - first:
				finalSum = subSum
				firstIndex = first
				endfirstIndex = i
	print firstIndex,endfirstIndex
	if allneg:
		return
	return A[firstIndex:endfirstIndex+1]


A = [-1,-1,-1,-2]
B = [-2, -3, 4, -1, -2, 1, 5, -3]
C = [2,4, 5, -7, 5, 3,2,1]
print maxNonNegSub(A)