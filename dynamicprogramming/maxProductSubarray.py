
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# Return an integer corresponding to the maximum product possible.
#
# Example :
#
# Input : [2, 3, -2, 4]
# Return : 6
#
# Possible with [2, 3]
def maxProduct(A):
	minimum = A[0]
	maximum = A[0]
	result = A[0]
	for i in range(1,len(A)):
		if A[i] < 0:
			maximum,minimum = minimum,maximum
		maximum = max(A[i],maximum*A[i])
		minimum = min(A[i],minimum*A[i])
		result = max(result,maximum)
	return result
A = [2,-3,-2]
print maxProduct(A)