# Write a function to find the longest common prefix string amongst an array of strings.
# Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.
# As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
# Given the array of strings, you need to find the longest S which is the prefix of ALL the strings in the array.
#
def Solution(l):
	if len(l) == 0:
		return ""
	if len(l) == 1:
		return l[0]
	minLength = 100000
	for i in range(len(l)): 
		if len(l[i]) < minLength:
			minLength = len(l[i])
	common = ""
	for i in range(minLength):
		curr = ""
		for string in l:
			if curr and curr != string[i]:
				return common
			else:
				curr = string[i]
		common += curr
	return common
l = ["abcdefgh","abefghijk","abcefgh","abriep"]
print Solution(l)