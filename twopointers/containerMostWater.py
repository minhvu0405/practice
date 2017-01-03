# Given n non-negative integers a1, a2, ..., an,
# where each represents a point at coordinate (i, ai).
# 'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Input : [1, 5, 4, 3]
# Output : 6

# Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
# So total area = 3 * 2 = 6
def Solution_BF(A):
	if len(A) < 2:
		return 0
	biggest = -1
	for i in range(len(A)):
		for j in range(i,len(A)):
			container = (j-i)*min(A[i],A[j])
			if container > biggest:
				biggest = container
	return biggest
def Solution(A):
	if len(A) < 2:
		return 0
	biggest = -1
	l = 0
	r = len(A) - 1
	while l < r:
		biggest = max(biggest,(r-l)*min(A[l],A[r]))
		if A[l] < A[r]:
			l += 1
		else:
			r -= 1
	return biggest
A = [1,5,4,3]
print Solution(A)