# longest increasing subarray
def longestIncreaseSubarray(arr):
	start = 0
	end = 0
	i = 1
	l = 1
	maxLen = -float('inf')
	while i < len(arr):	
		if arr[i] > arr[i-1]:
			end += 1
			l += 1
			if l > maxLen:
				maxLen = l
				indices = (start,end)
		else:
			start = i
			end = i
			l = 1
		i += 1
	return maxLen,indices
arr = [1,2,9,4,5,1,2,3,7]
print longestIncreaseSubarray(arr)