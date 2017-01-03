# You are given a set of coins S. In how many ways can you make sum
# N assuming you have infinite amount of each coin in the set.
#
# Note : Coins in set S will be unique. Expected space complexity of this problem is O(N).
#
# Example :
#
# Input :
# 	S = [1, 2, 3]
# 	N = 4
#
# Return : 4
#
# Explanation : The 4 possible ways are
# {1, 1, 1, 1}
# {1, 1, 2}
# {2, 2}
# {1, 3}
# Note that the answer can overflow. So, give us the answer % 1000007
def coin(S,N):
	if N == 0:
		return 1
	if N < 0:
		return 0
	if N >= 1 and len(S) < 1:
		return 0
	return coin(S[1:],N) + coin(S,N-S[0])
def coinSum(S,N):
	table = [[0 for i in range(len(S))] for j in range(N+1)]
	for i in range(len(S)):
		table[0][i] = 1
	for i in range(1,N+1):
		for j in range(len(S)):
			x = table[i][j-1] if j-1 >= 0 else 0
			y = table[i-S[j]][j] if i-S[j] >= 0 else 0
			table[i][j] = x + y
	return table[-1][-1]
def coinSumInfinite(S,N):
	table = [0 for i in range(N+1)]
	table[0] = 1
	for i in range(len(S)):
		for j in range(S[i],N+1):
			table[j] += table[j-S[i]]
		print table
	return table[-1]
S = [1, 2, 3]
N = 4
print coin(S,N)
print coinSum(S,N)
print coinSumInfinite(S,N)