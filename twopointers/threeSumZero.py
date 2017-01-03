# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
def threeSumZero(A):
	A = sorted(A)
	if len(A) < 3:
		return
	if len(A) == 3:
		if sum(A) == 0:
			return A
		else:
			return
	result = []
	for i in range(len(A)):
		if i == 0 or A[i] > A[i-1]:
			l = i + 1
			r = len(A) - 1
			while l < r:
				s = A[i] + A[l] + A[r]
				if  s == 0:
					result.append([A[i],A[l],A[r]])
					l += 1
					r -= 1
					while l < r and A[r] == A[r+1]:
						r -= 1
					while l < r and A[l] == A[l-1]:
						l += 1
				elif s > 0:
					r -= 1
				else:
					l += 1				
	return result

test = [ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
print threeSumZero(test)