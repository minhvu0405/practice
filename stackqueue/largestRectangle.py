# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1
# Find the area of largest rectangle in the histogram.
# For example, Given height = [2,1,5,6,2,3],
# return 10
def largestRectangle_BF(A):
	biggest = -float('inf')
	for i in range(len(A)):
		minCol = A[i]
		for j in range(i,len(A)):
			minCol = min(minCol,A[j])
			area = minCol*(j-i+1)
			biggest = max(biggest,area)
	return biggest
def largestRectangle(A):
	if len(A) < 1:
		return 0
	if len(A) == 1:
		return A[0]
	queue = []
	biggest = -float('inf')
	for i in range(len(A)):
		while queue and A[i] < A[queue[-1]]:
			h = queue.pop()
			if queue:
				area = A[h]*(i-queue[-1] - 1)
			else:
				area = A[h]*i
			biggest = max(biggest,area)
		queue.append(i)
	i += 1
	while queue:
		h = queue.pop()
		if queue:
			area = A[h]*(i-queue[-1] - 1)
		else:
			area = A[h]*i
		biggest = max(biggest,area) 
	return biggest
def largestRectangle_optimized(A):
	if len(A) < 1:
		return 0
	if len(A) == 1:
		return A[0]
	A = [-1] + A + [-1]
	queue = [0]
	biggest = -float('inf')
	for i in range(len(A)):
		while A[i] < A[queue[-1]]:
			h = queue.pop()
			area = A[h]*(i-queue[-1] - 1)
			biggest = max(biggest,area)
		queue.append(i)
	return biggest
t = [2,1,5,6,2,3]										 # 10
t1 = [6, 2, 5, 4, 5, 2, 6]								 # 14
t2 = [ 90, 58, 69, 70, 82, 100, 13, 57, 47, 18 ]		 # 348
t3 = [ 2, 82, 11, 89, 7, 21, 92, 13, 11, 94, 4, 96, 3 ]  # 96
print largestRectangle_BF(t3)
print largestRectangle(t3)
