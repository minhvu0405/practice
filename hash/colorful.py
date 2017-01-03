# For Given Number N find if its COLORFUL number or not
# Return 0/1
# A number can be broken into different contiguous sub-subsequence parts. 
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
# Example:

# N = 23
# 2 3 23
# 2 -> 2
# 3 -> 3
# 23 -> 6
# this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

# Output : 1
def Solve(A):
	s = str(A)
	myDict = {}
	for i in range(len(s)):
		mul = 1
		for j in range(i,len(s)):
			mul *= int(s[j])
			if mul in myDict:
				return False
			else:
				myDict[mul] = mul
	return True

print Solve(3245)