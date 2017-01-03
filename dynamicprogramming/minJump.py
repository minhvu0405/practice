# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example :
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
# If it is not possible to reach the end index, return -1.
def minJump_rec(A):
	def countJump(A,start,end):
		if start == end:
			return 0
		if A[start] == 0:
			return float('inf')
		minimum = float('inf')
		i = start + 1
		while i <= end and i <= start + A[start]:
			jumps = countJump(A,i,end)
			minimum = min(minimum,jumps+1)
			i += 1
		return minimum
	return countJump(A,0,len(A)-1)
def minJump(A):
	table = [float('inf')]*(len(A))
	table[0] = 0
	for i in range(1,len(A)):
		for j in range(0,i):
			if i <= j + A[j]:
				table[i] = min(table[i],table[j]+1)
				break
	return table[-1]

print minJump_rec([2,3,1,1,4])
print minJump_rec([1,3,5,8,9,2,6,7,6,8,9])
print minJump([1,3,5,8,9,2,6,7,6,8,9])