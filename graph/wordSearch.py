
def find(board,word):
	for i in range(len(board)):
		for j in range(len(board[0])):
			if dfs(board,word,i,j,0):
				return 1
	return 0
def dfs(board,word,i,j,k):
	if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
		return False
	if board[i][j] != word[k]:
		return False
	if k == len(word) - 1:
		return True
	elif dfs(board,word,i+1,j,k+1) or dfs(board,word,i-1,j,k+1) or dfs(board,word,i,j-1,k+1) or dfs(board,word,i,j+1,k+1):
		return True
	return False
board = [ "FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF" ]
word = "BCDCB"
print find(board,word)
# print exist(board,word)