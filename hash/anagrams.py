# Given an array of strings, return all groups of strings that are anagrams. 
# Represent a group by a list of integers representing the index in the original list. Look at the sample case for clarification.
# Input : cat dog god tca
# Output : [[1, 4], [2, 3]]
def Solve_Hash(A):
	result = []
	Dict = {}
	group = 0
	for i in range(len(A)):
		m = "".join(sorted(A[i]))
		if m not in Dict:
			Dict[m] = group
			group += 1
			result.append([i+1])
		else:
			result[Dict[m]].append(i+1)
	return result
A = ["cat", "dog", "god", "tca"]
print Solve_Hash(A)