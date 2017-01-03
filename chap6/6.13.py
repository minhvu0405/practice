def rotateArray(array,k):
	# Rotate to the left as default
	if array is None:
		return []
	k = k%len(array)
	# Rotate to the right
	# k = len(array)-k
	reverse(array,0,k-1)
	reverse(array,k,len(array)-1)
	reverse(array,0,len(array)-1)
def reverse(array,start,end):
	if array is None:
		return []
	while start < end:
		array[start],array[end] = array[end],array[start]
		start += 1
		end -= 1
def shift(array,k):
	result = []
	for i in range(len(array)):
		result.append(array[(i+k)%len(array)])
	return result
array = [1,2,3,4,5]
k = 2
print shift(array,k)
rotateArray(array,k)
print array
	