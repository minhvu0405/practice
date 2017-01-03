# Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.
# Do it in place.
# Example
# Given array A as
# 1 0 1
# 1 1 1 
# 1 1 1
# On returning, the array A should be :
# 0 0 0
# 1 0 1
# 1 0 1

def Solution(arr):
	x = [0]*len(arr[0])
	y = [0]*len(arr)
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if arr[i][j] == 1:
				x[j] = 1
				y[i] = 1
	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if x[j] == 1 or y[i] == 1:
				arr[i][j] = 1
	return arr
def Solution2(arr):
	firstRow = 0
	firstCol = 0
	lenRow = len(arr)
	if lenRow < 1:
		lenCol = 0
	else:
		lenCol = len(arr[0])
	for i in range(lenCol):
		if arr[0][i] == 0:
			firstRow = 1
			break
	for j in range(lenRow):
		if arr[j][0] == 0:
			firstCol = 1
			break
	for i in range(1,lenRow):
		for j in range(1,lenCol):
			if arr[i][j] == 0:
				arr[0][j] = 0
				arr[i][0] = 0
	for i in range(1,lenRow):
		for j in range(1,lenCol):
			if arr[0][j] == 0 or arr[i][0] == 0:
				arr[i][j] = 0
	if firstRow == 1:
		for i in range(lenCol):
			arr[0][i] = 0
	if firstCol == 1:
		for i in range(lenRow):
			arr[i][0] = 0
	return arr
arr = [[0,1,0],[0,0,0]]
arr1 = [[1,0,0,1],[0,0,1,0],[0,0,0,0]]
arr2 = [[0,0],[1,1]]
a = Solution2(arr2)
print a
