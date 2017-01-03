# You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

# Find i, j, k such that :
# max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
# Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
# Input : 
#         A : [1, 4, 10]
#         B : [2, 15, 20]
#         C : [10, 12]

# Output : 5 
#          With 10 from A, 15 from B and 10 from C. 

def Solution_BF(A,B,C):
	smallest = float('inf')
	for i in range(len(A)):
		for j in range(len(B)):
			for k in range(len(C)):
				smallest = min(max(abs(A[i]-B[j]),abs(B[j]-C[k]),abs(C[k]-A[i])),smallest)
	return smallest
def Solution(A,B,C):
	i = 0
	j = 0
	k = 0
	smallest = float('inf')
	while i < len(A) and j < len(B) and k < len(C):
		x = min(A[i],B[j],C[k])
		diff = max(A[i],B[j],C[k]) - x
		if diff < smallest:
			smallest = diff
		if x == A[i]:
			i += 1
		elif x == B[j]:
			j += 1
		else:
			k += 1
	return smallest
A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]
print Solution(A,B,C)