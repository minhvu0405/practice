def Solution(arr,L):
	if not arr:
		return []
	if L == 0:
		return [""]
	line = 0
	start = 0
	curr = 0
	split = []
	until = 0
	for i in range(len(arr)):
		if line + len(arr[i]) + 1 <= L:
			if line == 0:
				start = i
				line += len(arr[i])
			else:
				line += len(arr[i])+1
				curr = i
		else:
			split.append([start,curr])
			until = curr
			line = len(arr[i])
			start = i
			curr = 0
	if until < len(arr):
		split.append([start,len(arr)-1])
	n = len(split)
	res = []
	for i in range(n-1):
		res.append(justify(arr,split[i][0],split[i][1],L))
	start = split[n-1][0]
	end = split[n-1][1]
	lastline = ""
	for i in range(start,end):
		lastline += arr[i] + " "
	lastline += arr[end]
	left = L - len(lastline)
	lastline += " "*left
	res.append(lastline)
	return res
def justify(arr,start,end,L):
	numCharacters = 0
	numWords = 0
	for i in arr[start:end+1]:
		numCharacters += len(i)
		numWords += 1
	res = ""
	if numWords > 1:
		even = (L - numCharacters)/(numWords-1)
		left = (L - numCharacters)%(numWords-1)
		for i in range(start,end):
			if left:
				k = 1
				left -= 1
			else:
				k = 0
			res += arr[i] + " "*even + " "*k
		res += arr[end]
	else:
		res += arr[start]+ " "*(L - numCharacters)
	return res
arr = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16
# arr = [ "What", "must", "be", "shall", "be." ]
# L = 12
print Solution(arr,L)