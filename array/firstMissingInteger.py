# Given an unsorted integer array, find the first missing positive integer.
# Example:
# Given [1,2,0] return 3,
# [3,4,-1,1] return 2,
# [-8, -7, -6] returns 1
# Your algorithm should run in O(n) time and use constant space.
def splitNegPos(arr):
	n = len(arr)
	j = 0
	for i in range(n):
		if arr[i] <= 0:
			arr[i],arr[j] = arr[j],arr[i]
			j += 1
	return arr,j
def Solution(arr):
	arr, startPos = splitNegPos(arr)
	arr = arr[startPos:]
	size = len(arr)
	for i in range(size):
		if abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0:
			arr[abs(arr[i]) - 1] = - arr[abs(arr[i]) - 1]
	for i in range(size):
		if arr[i] > 0:
			return i+1
	return size+1
arr = [1,2,4,-1,4,-3,-7]
arr1 = [2, 3, 7, 6, 8, -1, -10, 15]
arr2 = [2, 3, -7, 6, 4, 1, -10, 15]
arr3 = [1, 1, 0, -1, -2]
print Solution(arr1)