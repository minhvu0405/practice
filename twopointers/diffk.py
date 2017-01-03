# Given an array ‘A’ of sorted integers and another non negative integer k
# find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
def Diffk(A,k):
	if k < 0:
		return 0
	if len(A) < 2:
		return 0
	i = 0
	j = 1
	while i < len(A) and j < len(A):
		s = A[j] - A[i]
		if s == k and i != j:
			return 1
		elif s < k:
			j += 1
		else:
			i += 1
	return 0
test = [ 1, 2, 2, 3, 4 ]
k = 2
print Diffk(test,k)