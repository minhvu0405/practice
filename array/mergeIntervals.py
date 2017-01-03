# Given a collection of intervals, merge all overlapping intervals.
# For example:
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# Make sure the returned intervals are sorted.
def myFN(x):
	return x[0]
def Solution(arr):
	if len(arr) < 1:
		return arr
	result = []
	arr = sorted(arr,key=myFN)
	pre = arr[0]
	for i in range(1,len(arr)):
		curr = arr[i]
		if curr[0] <= pre[1]:
			temp = [min(curr[0],pre[0]),max(curr[1],pre[1])]
			pre = temp
		else:
			result.append(pre)
			pre = curr
	result.append(pre)
	result = sorted(result,key=myFN)
	return result
arr1 = [[1,3],[2,4],[5,7],[6,8]]
arr2 = [[6,8], [1,9], [2,4], [4,7]]
arr3 = [[1,4],[4,5],[3,6],[7,9],[8,11]]
arr4 = [[1,3],[6,9],[2,5]]
arr5 = [[1,2],[3,5],[6,7],[8,10],[12,16],[4,9]]
arr6 = [[1,3],[2,6],[8,10],[15,18]]
print Solution(arr6)


