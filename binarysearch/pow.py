def Solution(x,y):
	if y == 0:
		return 1
	base = x
	result = 1
	i = 1
	while y > 0:
		if y%2 == 1:
			result = result*base
		base = base*base
		y = y/2
	return result
print Solution(3,5)