# Input : [4 5 6 7 0 1 2] and target = 4
# Output : 0
def Solution(arr,target):
	start = 0
	end = len(arr) - 1
	while start <= end:
		mid = (start + end)/2
		i = mid - 1
		j = mid + 1
		if arr[mid] == target:
			return mid
		if arr[start] <= arr[mid]:
			if arr[start] <= target and target <= arr[mid]:
				end = mid - 1
			else:
				start = mid + 1
		else:
			if arr[mid] <= target and target <= arr[end]:
				start = mid + 1
			else:
				end = mid - 1
	return -1
arr = [4,5,7,0,1,2]
target = 7
print Solution(arr,target)