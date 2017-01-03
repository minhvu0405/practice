# Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.
def Solution(A):
	if not A:
		return 0
	curr = 0
	count = 0
	i = 0
	while i < len(A):
		if i == 0 or A[i] != A[i-1]:
			A[curr] = A[i]
			curr += 1
			count = 1
		else:
			if count == 1:
				A[curr] = A[i]
				curr += 1
				count += 1
		i += 1
	A = A[:curr] 
	return curr
print Solution([1,1,1,2,3,3,3])


