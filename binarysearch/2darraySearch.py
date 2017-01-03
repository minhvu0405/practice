# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
def Solution(arr,x):
	start = 0
	end = len(arr[0])*len(arr)-1
	while start <= end:
		mid = (start+end)/2
		i = mid/len(arr[0])
		j = mid%len(arr[0])
		if x == arr[i][j]:
			return 1
		elif x > arr[i][j]:
			j += 1
			start = i*len(arr[0]) + j
		else:
			j -= 1
			end = i*len(arr[0]) + j
	return 0
arr = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
print Solution(arr,50)