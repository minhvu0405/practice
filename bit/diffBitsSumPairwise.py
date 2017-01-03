def Solution(inlist):
	n = len(inlist)
	total = 0
	for i in range(32):
		count = 0
		for j in range(n):
			if inlist[j] & 1:
				count += 1
			inlist[j] >>= 1
		total += count*(n-count)*2
	return total % (10**9 + 7)
print Solution([1,3,5])