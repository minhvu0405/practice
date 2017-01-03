# Given 2 sorted arrays, find all the elements which occur in both the arrays.
def Solution(A,B):
	if len(A) == 0 or len(B) == 0:
		return []
	i = 0
	j = 0
	result = []
	while i < len(A) and j < len(B):
		if A[i] == B[j]:
			result.append(A[i])
			i += 1
			j += 1
		elif A[i] > B[j]:
			j += 1
		else:
			i += 1
	return result
A = [1,2,3,3,4,5,6]
B = [3,5]
print Solution(A,B)