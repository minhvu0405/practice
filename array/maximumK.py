# Given an array of positive integers, find maximum possible value K such that the array has at-least 
# K elements that are greater than or equal to K. The array is unsorted and may contain duplicate values.

def Solution(arr):
	arr = sorted(arr)
	print "arr: ",arr
	maximum = 0
	index = -1
	numElements = -1
	n = min(arr) - 1
	for i in range(len(arr)):
		if arr[i] <= len(arr) - i:
			numElements = len(arr)-i
			index = i
	if index != -1:
		return arr[index]
	return n

print Solution([2,3,4,5,6,7])
print Solution([1, 2, 3, 4])
print Solution([4, 7, 2, 3, 8])
print Solution([6, 7, 9, 8, 10])