# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
# Note that when the count of a character C in T is N, then the count of C in minimum window in S should be at least N.
def Solve(A,B):
	if len(A) < len(B):
		return
	counter = {}
	target = {}
	for i in range(len(B)):
		if B[i] not in target:
			target[B[i]] = 1
		else:
			target[B[i]] += 1
	for i in range(len(B)):
		if B[i] not in counter:
			counter[B[i]] = 0
	cover = 0
	full = len(counter)
	i = 0
	start = 0
	infor = None
	while i < len(A) or cover == full:
		if cover < full:
			if A[i] in target:
				counter[A[i]] += 1
				if target[A[i]] == counter[A[i]]:
					cover += 1
			i += 1
		else:
			if A[start] in target:
				counter[A[start]] -= 1
				if target[A[start]] - 1 == counter[A[start]]:
					cover -= 1
			start += 1
		if cover == full:
			if infor is None or i-start < infor[0]:
				infor = i - start, start, i
	if infor is None:
		return
	return A[infor[1]:infor[2]]
S = "ADOBECODEBANC"
T = "ABC"
print Solve(S,T)