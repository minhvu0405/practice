
def Solution(A,B,k):
	lenA = len(A)
	lenB = len(B)
	if lenA > lenB:
		return Solution(B,A,k)
	if lenA == 0:
		return B[k-1]
	if k == 1:
		return min(A[0],B[0])
	a = min(k/2,lenA)
	b = k - a
	if A[a-1] <= B[b-1]:
		return Solution(A[a:],B,b)
	return Solution(A,B[b:],a)
A = [1,2,3,5,6,7,8]
B = [2,3,5,7,9]
k = 2
C = sorted(A+B)
print C
print Solution(A,B,k)
print C[k-1]