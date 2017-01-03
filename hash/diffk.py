# Given an array A of integers and another non negative integer k
# find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
def Solve_BF(A,k):
	if len(A) < 2:
		return 0
	for i in range(len(A)-1):
		for j in range(len(A)):
			if i != j and A[i] - A[j] == k:
				return 1
	return 0
def Solve_Hash(A,k):
	if len(A) < 2:
		return 0
	Dict = {}
	for i in range(len(A)):
		if A[i] not in Dict:
			Dict[A[i]] = 1
		else:
			Dict[A[i]] += 1
	for i in range(len(A)):
		if (k != 0 and A[i] - k in Dict) or (k == 0 and Dict[A[i]] > 1): 
			return 1
	return 0
def Solve(A,k):
	if len(A) < 2:
		return 0
	A.sort()
	left = 0
	right = 1
	while left < len(A) and right < len(A):
		if left != right and A[right] - A[left] == k:
			return 1
		elif A[right] - A[left] < k:
			right += 1
		else:
			left += 1
	return 0
# A = [ 66, 37, 46, 56, 49, 65, 62, 21, 7, 70, 13, 71, 93, 26, 18, 84, 96, 65, 92, 69, 97, 47, 6, 18, 17, 47, 28, 71, 70, 24, 46, 58, 71, 21, 30, 44, 78, 31, 45, 65, 16, 3, 22, 54, 51, 68, 19, 86, 44, 99, 53, 24, 40, 92, 38, 81, 4, 96, 1, 13, 45, 76, 77, 8, 88, 50, 89, 38, 60, 61, 49, 25, 10, 80, 49, 63, 95, 74, 29, 27, 52, 27, 40, 66, 38, 22, 85, 22, 91, 98, 19, 20, 78, 77, 48, 63, 27 ]
# k = 31
# A = [ 11, 85, 100, 44, 3, 32, 96, 72, 93, 76, 67, 93, 63, 5, 10, 45, 99, 35, 13 ]
# k = 60
A = [ 80, 87, 75, 11, 57, 31, 88, 48, 15, 77, 44, 22, 82, 41, 52, 52, 99, 40, 84, 21, 30, 100, 61, 48, 96, 64, 73, 79, 84, 95, 14, 48, 80, 90, 26, 97, 33, 88, 25, 84, 85, 57, 44, 91, 64, 16, 39, 30, 18, 17, 84, 54, 54, 50, 24, 13, 100, 80, 69, 22, 96, 12, 68, 65, 40, 47, 70, 48, 53, 10, 39, 61, 56, 11, 46, 18, 94, 49, 59, 31, 30, 16, 64, 90, 90 ]
k = 1
# A = [ 1, 3, 2 ]
# k = 0
print Solve_BF(A,k)
print Solve(A,k)
print Solve_Hash(A,k)