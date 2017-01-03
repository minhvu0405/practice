# Given a string, 
# find the length of the longest substring without repeating characters.
# Example:
# The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
def Solve_BF(s):
	if len(s) < 2:
		return len(s)
	maxLen = 1
	for i in range(len(s)-1):
		for j in range(i+1,len(s)):
			visited = {}
			flag = False
			for k in range(i,j+1):
				if s[k] not in visited:
					visited[s[k]] = 1
				else:
					flag = True
			if flag == False:
				if maxLen < len(s[i:j+1]):
					maxLen = len(s[i:j+1])
	return maxLen

def Solve(s):
	if len(s) < 2:
		return len(s)
	visited = {}
	visited[ord(s[0])] = 0
	currLen = 1
	maxLen = 1
	for i in range(1,len(s)):
		m = ord(s[i])
		if m not in visited or (m in visited and visited[m] < i - currLen):
			currLen += 1
		else:
			maxLen = max(maxLen,currLen)
			currLen = i - visited[m]
		visited[m] = i
	maxLen = max(maxLen,currLen)
	return maxLen
s = "abcabcbb"
s = "bbbbb"
s = "ABDEFGABEF"
s = "dadbc"
print Solve_BF(s)
print Solve(s)