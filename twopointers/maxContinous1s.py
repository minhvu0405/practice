def Solution_BF(A,m):
	maxLength = 0
	result = []
	for i in range(len(A)):
		count_zero = 0
		for j in range(i,len(A)):
			if A[j] == 0:
				count_zero += 1
			if count_zero <= m:
				if j - i > maxLength:
					maxLength = j - i
					result = range(i,j)
			else:
				break
	return result
def Solution(A,m):
	l = 0
	r = 0
	count_zero = 0
	maxLength = 0
	result = None
	while r < len(A):
		if A[r] == 0:
			count_zero += 1
		if count_zero == m + 1:
			length = r-1 - l + 1
			if length > maxLength:
				maxLength = length
				result = range(l,r)
			while A[l] != 0 and l < r:
				l += 1	
			l += 1
			count_zero -= 1
		r += 1
	if count_zero <= m:
		if r-1 - l > maxLength:
			result = range(l,r)
	return result
def AnotherSolution(A,m):
	l = 0
	r = 0
	count_zero = 0
	maxLength = 0
	result = []
	while r < len(A):
		if count_zero <= m:
			if A[r] == 0:
				count_zero += 1
			r += 1
		if count_zero > m:
			if A[l] == 0:
				count_zero -= 1
			l += 1
		if count_zero <= m and r - l + 1 > maxLength:
			maxLength = r - l + 1
			result = range(l,r)
	return result

A = [1,1,0,1,1,0,0,1,1,1,1]
m = 2
print Solution(A,m)
print AnotherSolution(A,m)