# Compute the maximum difference (A[j] - A[i]) + (A[k] - A[l]), subject to i < j < k < l
def maxDiff(arr):
	left = [0]*len(arr)
	right = [0]*len(arr)
	min_so_far = arr[0]
	max_so_far = arr[len(arr)-1]
## use 2n spaces
	for i in range(1,len(arr)):
		min_so_far = min(arr[i],min_so_far)
		left[i] = arr[i] - min_so_far
	for i in range(len(arr)-2,-1,-1):
		max_so_far = max(arr[i+1],max_so_far)
		right[i] = max_so_far - arr[i+1]
	maxDiff = 0
	for i in range(len(arr)):
		maxDiff = max(maxDiff,left[i]+right[i])
## save n spaces
	# min_so_far = float('inf')
	# for i in range(len(arr)):
	# 	min_so_far = min(arr[i],min_so_far)
	# 	maxDiff = max(maxDiff,arr[i]-min_so_far + right[i])
	return maxDiff
arr = [1,3,2,5,2,4,9,7]
arr = [9,8,7,6,5,4,3,2,1]
print maxDiff(arr)