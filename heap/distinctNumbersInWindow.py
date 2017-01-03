# You are given an array of N integers, A1, A2 ,...,An 
# and an integer K. Return the of count of distinct numbers in all windows of size K.
#
# Formally, return an array of size N-K+1 where ith
# element in this array contains number of distinct elements in sequence Ai, Ai+1,...,Ai+k-1
# Note:
# - If K > N, return empty array.
#
# For example,
#
# A=[1, 2, 1, 3, 4, 3] and K = 3
#
# All windows of size K are
#
# [1, 2, 1]
# [2, 1, 3]
# [1, 3, 4]
# [3, 4, 3]
#
# So, we return an array [2, 3, 3, 2].
def Solve(arr,k):
	result = []
	if len(arr) < 1:
		return result
	if len(arr) < k:
		return result
	myDict = {}
	for i in range(len(arr)):
		if arr[i] in myDict:
			myDict[arr[i]] += 1
		else:
			myDict[arr[i]] = 1
		if i - k + 1 >= 0:
			result.append(len(myDict))
			myDict[arr[i-k+1]] -= 1
			if myDict[arr[i-k+1]] == 0:
				myDict.pop(arr[i-k-1])
	return result
print Solve([1, 2, 1, 3, 4, 3],3)