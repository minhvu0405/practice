def Solution(arr,dep,k):
	if len(arr) != len(dep):
		return False
	n = len(arr)
	if n < 1:
		return False
	arr.sort()
	dep.sort()
	i = 0
	j = 0
	curr = 0
	while i < n and j < n:
		if arr[i] < dep[j]:
			curr += 1
			i += 1
			if curr > k:
				return False
		else:
			curr -= 1
			j += 1
	return True
arr = [1,2,3]
dep = [2,3,4]
k = 1
print Solution(arr,dep,k)