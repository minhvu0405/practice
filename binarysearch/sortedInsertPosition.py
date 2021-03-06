
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Here are few examples.
# [1,3,5,6], 5 -> 2
# [1,3,5,6], 2 -> 1
# [1,3,5,6], 7 -> 4
# [1,3,5,6], 0 -> 0
def Solution(arr,x):
	if len(arr) == 0:
		return 
	start = 0
	end = len(arr) - 1
	while start <= end:
		mid = (start+end)/2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			end = mid - 1
		else:
			start = mid + 1

	return start
arr = [1,3,5,6]
print Solution(arr,5)
print Solution(arr,2)
print Solution(arr,7)
print Solution(arr,0)