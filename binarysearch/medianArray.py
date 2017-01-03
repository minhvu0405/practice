# There are two sorted arrays A and B of size m and n respectively.
# Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
# The overall run time complexity should be O(log (m+n)).
# Sample Input
# A : [1 4 5]
# B : [2 3 6]			
# Sample Output
# 3
import numpy
def Solution(A,B): 		# Case m == n
	while len(A) != 2 or len(B) != 2:
		mA = median(A)
		mB = median(B)
		print mA,mB
		if mA == mB:
			return mA
		elif mA > mB:
			if len(A) % 2 == 0:
				A = A[:len(A)/2+1]
				B = B[len(B)/2-1:]
			else:
				A = A[:len(A)/2+1]
				B = B[len(B)/2:]
		else:
			if len(A) % 2 == 0:
				A = A[len(A)/2-1:]
				B = B[:len(B)/2+1]
			else:
				A = A[len(A)/2:]
				B = B[:len(B)/2+1]
	print A,B
	mean = (max(A[0],B[0]) + min(A[1],B[1]))/2.0
	return mean
def Solution2(A,n,B,m):	
	if n == 0:
		return medianSingle(B,m)
	if n == 1:
		if m == 1:
			return medianof2(A[0],B[0])
		elif m%2 != 0:
			return medianof2(B[m/2],medianof3(A[0],B[m/2-1],B[m/2+1]))
		else:
			return medianof3(B[m/2],B[m/2-1],A[0])
	elif n == 2:
		if m == 2:
			return medianof4(A[0],A[1],B[0],B[1])
		elif m%2 != 0:
			return medianof3(B[m/2],max(A[0],B[m/2-1]),min(A[1],B[m/2+1]))
		else:
			print A,B
			return medianof4(B[m/2],B[m/2 -1],max(A[0],B[m/2-2]),min(A[1],B[m/2+1]))
	idxA = (n-1)/2
	idxB = (m-1)/2
	print idxA,idxB
	if A[idxA] <= B[idxB]:
		return Solution2(A[idxA:],n/2+1,B[:idxB+1],m-idxA)
	return Solution2(A[:idxA+1],n/2+1,B[idxB:],m-idxA)
def medianSortedArrays(A,B):
	if len(A) > len(B):
		return Solution2(B,len(B),A,len(A))
	return Solution2(A,len(A),B,len(B))
def medianSingle(X,i):
	if i == 0:
		return -1
	if i%2 == 0:
		return X[i/2] + X[i/2 -1]
	return X[i/2]
def medianof2(a,b):
	return (a+b)/2.0
def medianof3(a,b,c):
	return (a+b+c) - max(a,max(b,c)) - min(a,min(b,c))
def medianof4(a,b,c,d):
	return ((a+b+c+d) - max(a,max(b,max(c,d))) - min(a,min(b,min(c,d))))/2.0
def median(arr):
	n = len(arr)
	if n%2 == 0:
		return (arr[n/2] + arr[(n/2)-1])/2
	return arr[n/2]

# A = [1,4,5,6]
# B = [2,3,7,9]
# A = [ -50, -47, -36, -35, 0, 13, 14, 16 ]
# B = [ -31, 1, 9, 23, 30, 39]
A = [ -50, -41, -40, -19, 5, 21, 28 ]
B = [ -50, -21, -10 ]
C = A + B
C = sorted(C)
print C
print medianSortedArrays(A,B) 
# print Solution(A,B)
print numpy.median(C)
# print Solution2([ -50, -47, -36, -35, 0, 13, 14, 16 ],[ -31, 1, 9, 23, 30, 39 ])



