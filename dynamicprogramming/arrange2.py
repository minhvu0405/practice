# You are given a sequence of black and white horses, and a set of K stables numbered 1 to K. 
# You have to accommodate the horses into the stables in such a way that the following conditions are satisfied:
# You fill the horses into the stables preserving the relative order of horses.
# For instance, you cannot put horse 1 into stable 2 and horse 2 into stable 1. 
# You have to preserve the ordering of the horses.
# No stable should be empty and no horse should be left unaccommodated.
# Take the product (number of white horses * number of black horses) for each stable and take the sum of all these products. 
# This value should be the minimum among all possible accommodation arrangements
# Input: {WWWB} , K = 2
# Output: 0

# Explanation:
# We have 3 choices {W, WWB}, {WW, WB}, {WWW, B}
# for first choice we will get 1*0 + 2*1 = 2.
# for second choice we will get 2*0 + 1*1 = 1.
# for third choice we will get 3*0 + 0*1 = 0.

# Of the 3 choices, the third choice is the best option.
def arrange(S,K):
	cache = {}
	if len(S.strip()) < K:
		return -1
	def arrange_util(s,k):
		if k == 1:
			count = 0
			for i in s:
				if i == "W":
					count += 1
			cache[(K-k,len(s))] = count*(len(s)-count)
			return cache[(K-k,len(s))]
		else:
			if (K-k,len(s)) not in cache:
				maxPosition = len(s) - k + 1
				cache[(K-k,len(s))] = float('inf')
				count = 0
				for i in range(maxPosition):
					if s[i] == "W":
						count += 1
					cache[(K-k,len(s))] = min(count*(maxPosition-count)+arrange_util(s[i+1:],k-1),cache[(K-k,len(s))])
			return cache[(K-k,len(s))]
	return arrange_util(S,K)
print arrange("WWWB",2)