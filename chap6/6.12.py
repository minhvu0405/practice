def nextPermutation(array):
	if len(array) < 1:
		return []
	p = -1
	for i in range(len(array)-2,-1,-1):
		if array[i] < array[i+1]:
			p = i
			break
	if p == -1:
		return sorted(array)
	q = p+1
	for i in range(len(array)-1,p,-1):
		if array[i] > p:
			q = i
			break
	array[p],array[q] = array[q],array[p]
	array = array[:p+1] + sorted(array[p+1:])
	return array
a = [1,2,3,1]
b = [3,2,1]
c = [1,1,4]
print nextPermutation(a)