# Given an array of integers, sort the array into a wave like array and return it, 
# In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

# Example

# Given [1, 2, 3, 4]

# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]
def Solution(arr):
	arr = sorted(arr)
	temp = None
	for i in range(1,len(arr),2):
		arr[i], arr[i-1] = arr[i-1], arr[i]
	return arr
def Solution2(arr):
	n = len(arr)
	for i in range(0,n,2):
		if i > 0 and arr[i] > arr[i-1]:
			arr[i],arr[i-1] = arr[i-1],arr[i]
		if i < n - 1 and arr[i] > arr[i+1]:
			arr[i],arr[i+1] = arr[i+1],arr[i]
	return arr
arr = [2,5,7,8,81,42,4,6,31,0,5,3,21,7,42]
print Solution2(arr)