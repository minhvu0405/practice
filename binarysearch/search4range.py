# Given a sorted array of integers, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n)
# If the target is not found in the array, return [-1, -1].
# Example:
# Given [5, 7, 7, 8, 8, 10]
# and target value 8,
# return [3, 4].
def Solution(arr,x):
	if len(arr) == 0:
		return [-1,-1]
	start = 0
	end = len(arr) - 1
	StartBound = -1
	while start <= end:
		mid = (start+end)/2
		if arr[mid] == x:
			end = mid - 1
			StartBound = mid
		elif arr[mid] > x:
			end = mid - 1
		else:
			start = mid+1
	if StartBound == -1:
		return [-1,-1]
	start = end
	end = len(arr) -1
	EndBound = -1
	while start <= end:
		mid = (start+end)/2
		if arr[mid] == x:
			start = mid + 1
			EndBound = mid
		elif arr[mid] > x:
			end = mid - 1
		else:
			start = mid+1
	if EndBound == -1:
		return [-1,-1]
	return [StartBound,EndBound]
arr = [5, 7, 7, 8, 8,8, 10]
print Solution(arr,7)

