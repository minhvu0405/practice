import copy
def Solve(A,l,r,result):
	if l == r-1:
		result.append(copy.copy(A))
		return
	for i in range(l,r):
		A[l],A[i] = A[i],A[l]
		Solve(A,l+1,r,result)
		A[l],A[i] = A[i],A[l]

A = ['A','B','C']
result = []
Solve(A,0,len(A),result)
print result
