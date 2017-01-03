def DutchNationFlag(array,n):
	if n < 0 or n >= len(array):
		return array
	left = 0
	right = len(array)-1
	temp = array[n]
	i = 0
	while i <= right:
		if array[i] > temp:
			array[i],array[right] = array[right],array[i]
			right -= 1
		elif array[i] < temp:
			array[i],array[left] = array[left],array[i]
			left += 1
			i += 1
		else:
			i += 1
	return array
print DutchNationFlag([5,13,3,2,7,8],0)