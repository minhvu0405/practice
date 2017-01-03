# Remove duplicates from Sorted Array
# Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.
def Solution(A):
	curr = 0
	for i in range(0,len(A)):
		if A[i] == 0 or A[i] != A[i-1]:
			A[curr] = A[i]
			curr += 1
	print A[:curr]
	return curr
A = [1,1,1,2]
print Solution(A)