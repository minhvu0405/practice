# Given an array with n objects colored red, white or blue, 
# sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
def Solution1(A):
	if len(A) < 1:
		return A
	count_zero = 0
	count_one = 0
	for i in range(len(A)):
		if A[i] == 0:
			count_zero += 1
		elif A[i] == 1:
			count_one += 1
	for i in range(len(A)):
		if i < count_zero:
			A[i] = 0
		elif count_zero <= i < count_zero + count_one:
			A[i] = 1
		else:
			A[i] = 2
	return A
def Solution2(A):
	if len(A) < 1:
		return []
	l = 0
	m = 0
	r = len(A) - 1
	while m <= r:
		if A[m] == 0:
			A[l],A[m] = A[m],A[l]
			l += 1
			m += 1
		elif A[m] == 2:
			A[r],A[m] = A[m],A[r]
			r -= 1
		else:
			m += 1
	return A
A = [ 2, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 0, 1 ]

print Solution2(A)