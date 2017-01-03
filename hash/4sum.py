# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
# The solution set must not contain duplicate quadruplets.
def Solve(A,target):
	if len(A) < 4:
		return []
	result = []
	A.sort()
	for i in range(len(A)-3):
		if i > 0  and A[i] == A[i-1]:
			continue
		for j in range(i+1,len(A)-2):
			if j > i+1 and A[j] == A[j-1]:
				continue
			left = j+1
			right = len(A)-1
			while left < right:
				m = A[i] + A[j] + A[left] + A[right]
				if m == target:
					temp = A[i],A[j],A[left],A[right]
					result.append(temp)
					left += 1
					while left < right and A[left] == A[left-1]:
						left += 1
				elif m > target:
					right -= 1
				else:
					left += 1
	return result

A = [ 9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2 ]
target = 0
print Solve(A,target)