# Implement the next permutation, which rearranges numbers into the numerically next greater permutation of numbers.
# If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted in an ascending order.
# The replacement must be in-place, do not allocate extra memory.
# Examples:
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 20, 50, 113 → 20, 113, 50
def Solution(A):
    if len(A) < 1:
        return A
    k = -1
    for i in range(1,len(A)):
        if A[i-1] < A[i]:
            k = i - 1
    if k == -1:
        return sorted(A)
    l = -1
    for j in range(len(A)):
        if A[j] > A[k]:
            l = j
    A[k],A[l] = A[l],A[k]
    print A
    x = sorted(A[k+1:])
    A = A[:k+1] + x
    return A
def reverse(A):
	n = len(A)/2
	for i in range(n):
		A[i], A[len(A) - i - 1] = A[len(A) - i - 1], A[i] 
	return A
A = [1,2,3,1,6]
print Solution(A)