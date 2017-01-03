
# Find the longest increasing subsequence of a given sequence / array.
#
# In other words, find a subsequence of array in which the
# subsequence's elements are in strictly increasing order,
# and in which the subsequence is as long as possible.
# This subsequence is not necessarily contiguous, or unique.
# In this case, we only care about the length of the longest increasing subsequence.
#
# Example :
#
# Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# Output : 6
# The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]

def longestIncreaseSubsequence(A):
	if len(A) < 1:
		return 0
	table = [1]*len(A)
	for i in range(1,len(A)):
		for j in range(0,i):
			if A[j] < A[i]:
				table[i] = max(table[i],table[j]+1)
	return max(table)
def LIS_displaySequence(A):
	if len(A) < 1:
		return 0
	table = [[] for i in range(len(A))]
	table[0].append(A[0])
	for i in range(1,len(A)):
		for j in range(0,i):
			if A[j] < A[i] and len(table[i]) < len(table[j]) + 1:
				table[i] = table[j][:]
		table[i].append(A[i])
	maximum = []
	for i in table:
		if len(i) > len(maximum):
			maximum = i 
	return maximum
print longestIncreaseSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
print LIS_displaySequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])