# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 < index2. Please note that your returned answers (both index1 and index2 ) are not zero-based. 
# Put both these numbers in order in an array and return the array from your function ( Looking at the function signature will make things clearer ). Note that, if no pair exists, return empty list.

# If multiple solutions exist, output the one where index2 is minimum. If there are multiple solutions with the minimum index2, choose the one with minimum index1 out of them.
# Input: [2, 7, 11, 15], target=9
# Output: index1 = 1, index2 = 2
def Solve(A,target):
	if len(A) < 2:
		return []
	myDict = {}
	for i in range(len(A)):
		n = target - A[i]
		if n in myDict:
			return [myDict[n]+1,i+1]
		else:
			if A[i] not in myDict:
				myDict[A[i]] = i
	return []
# A = [1,8, 2, 7, 11, 15]
A = [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
target = -3
print Solve(A,target)