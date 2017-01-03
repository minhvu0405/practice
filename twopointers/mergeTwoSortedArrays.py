# Given two sorted integer arrays A and B, merge B into A as one sorted array.
def Solution(A,B):
	a = len(A) - 1
	b = len(B) - 1
	for i in range(len(B)):
		A.append(0)	
	curr = len(A) - 1
	while b >= 0 and a >= 0:
		if A[a] > B[b]:
			A[curr] = A[a]
			a -= 1
			curr -= 1
		else:
			A[curr] = B[b]
			b -= 1
			curr -= 1
	while a >= 0:
		A[curr] = A[a]
		a -= 1
		curr -= 1
	while b >= 0:
		A[curr] = B[b]
		b -= 1
		curr -= 1
	return A
A = [ 1, 2 ]
B = [ -1, 2 ]
print Solution(A,B)

