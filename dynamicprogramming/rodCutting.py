def rodCutting(price,length):
	if length == 0:
		return 0
	q = -float('inf')
	for i in range(length):
		q = max(q,price[i]+rodCutting(price,length-i-1))
	return q
def rodCutting_DP(price,length):
	r = [0]*(length+1)
	for i in range(1,length+1):
		q = -float('inf')
		for j in range(i):
			q = max(q,price[j]+r[i-j-1])
		r[i] = q
	return r[-1]

price = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
print rodCutting(price,n)
print rodCutting_DP(price,n)
