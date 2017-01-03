# Find minimum number of coins that make a given value
def minimumCoin(A,target):
	if target <= 0:
		return 0
	result = float('inf')
	for i in range(len(A)):
		m = min(result,1+minimumCoin(A,target-A[i]))
		if m < result:
			result = m
	return result
def minimumCoin_DP(A,target):
	table = [float('inf')]*(target+1)
	table[0] = 0
	for i in range(target+1):
		for j in range(len(A)):
			table[i] = min(table[i],table[i-A[j]] + 1)
	return table[-1]
# A = [1,5,6,9]
# target = 11
A = [25,10,5]
target = 30
print minimumCoin(A,target)
print minimumCoin_DP(A,target)