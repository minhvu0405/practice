def distinctSubsequence(A,B):
	table = [[0 for i in range(len(B)+1)] for j in range(len(A)+1)]
	for i in range(len(A)+1):
		table[i][0] = 1
	for i in range(1,len(A)+1):
		for j in range(1,len(B)+1):
			table[i][j] = table[i-1][j]
			if A[i-1] == B[j-1]:
				table[i][j] += table[i-1][j-1]
	return table
print distinctSubsequence('abc','ac')