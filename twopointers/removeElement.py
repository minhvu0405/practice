# Given an array and a value, remove all the instances of that value in the array. 
# Also return the number of elements left in the array after the operation.
# It does not matter what is left beyond the expected length.
def Solution(A,x):
	if len(A) < 1:
		return 0
	curr = 0
	for i in range(len(A)):
		if A[i] != x:
			A[curr] = A[i]
			curr += 1
	return curr
# A = [4,1,1,2,1,3]
# e = 1
A = [0]
e = 0
print Solution(A,e)