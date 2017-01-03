# Given two words A and B, find the minimum number of
# steps required to convert A to B. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# Insert a character
# Delete a character
# Replace a character
# Example :
# edit distance between
# "Anshuman" and "Antihuman" is 2.
#
# Operation 1: Replace s with t.
# Operation 2: Insert i.
def editDistance_rec(A,B):
	if len(A) == 0:
		return len(B)
	if len(B) == 0:
		return len(A)
	if A[-1] == B[-1]:
		return editDistance_rec(A[:-1],B[:-1])
	return 1 + min(editDistance_rec(A,B[:-1]),editDistance_rec(A[:-1],B),editDistance_rec(A[:-1],B[:-1]))
def editDistance(A,B):
	table = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
	for i in range(len(B)+1):
		for j in range(len(A)+1):
			if i == 0:
				table[i][j] = j
			elif j == 0:
				table[i][j] = i
			elif B[i-1] == A[j-1]:
				table[i][j] = table[i-1][j-1]
			else:
				table[i][j] = 1 + min(table[i][j-1],table[i-1][j],table[i-1][j-1])
	return table[-1][-1]
print editDistance_rec('abcd','ab1cd')
print editDistance_rec('ab','opabcdef')
print editDistance_rec('sunday','saturday')
print editDistance('abcd','ab1cd')
print editDistance('ab','opabcdef')
print editDistance('sunday','saturday')