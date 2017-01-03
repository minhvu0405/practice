# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
# The input corresponding to the above configuration :
# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
def Solve(A):
	col = [{} for i in range(9)]
	row = [{} for i in range(9)]
	sub = [{} for i in range(9)]
	for i in range(len(A)):
		for j in range(len(A[0])):
			if A[i][j] not in col[j]:
				col[j][A[i][j]] = True
			else:
				return 0
			if A[i][j] not in row[i]:
				row[i][A[i][j]] = True
			else:
				return 0
			subNumber = 3*(i/3) + (j/3)
			if A[i][j] not in sub[subNumber]:
				sub[subNumber][A[i][j]] = True
			else:
				return 0
	return 1
A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
print Solve(A)