def bruteforce(s):
	if len(s) <= 1:
		return s
	maximum = 1
	index = 0
	for i in range(len(s)-1):
		for j in range(i,len(s)):
			if isPalindrome(s[i:j+1]):
				if len(s[i:j+1]) > maximum:
					maximum = len(s[i:j+1])
					index = i
	return s[index:index+maximum]
def isPalindrome(s):
	for i in range(len(s)/2):
		if s[i] != s[len(s)-1-i]:
			return False
	return True
def findLongestPalindrome(s):
	if len(s) <= 1:
		return s
	maximum = 1
	index = 0
	for i in range(1,len(s)):
		j = i-1
		k = i
		count = 0
		while 0 <= j and k < len(s) and s[j] == s[k]:
			count = k - j + 1
			if count > maximum:
				maximum = count
				index = j
			k += 1
			j -= 1

		j = i-1
		k = i+1
		count = 0
		while 0 <= j and k < len(s) and s[j] == s[k]:
			count = k - j + 1
			if count > maximum:
				maximum = count
				index = j
			k += 1
			j -= 1
	return s[index:index+maximum]
s = "aaaabaaa"
s = "abcdd"
# print bruteforce(s)
print findLongestPalindrome(s)