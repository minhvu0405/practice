
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return 1 ( true ).
#
# A = [3,2,1,0,4], return 0 ( false ).
#
# Return 0/1 for this problem
def jumpGame(A):
	maxJump = -float('inf')
	for i in range(len(A)-1):
		maxJump = max(maxJump,A[i]+i)
		if maxJump == i:
			return 0
	return 1
print jumpGame([2,3,1,1,4])
print jumpGame([3,2,1,0,4])