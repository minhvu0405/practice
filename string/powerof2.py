# Find if Given number (string) is power of 2 or not.
# More specifically, find if given number can be expressed as 2^k where k >= 1.
def Solution(s):
	s = list(s)
	s = removeZerors(s)
	if len(s) == 0:
		return False
	if isOdd(s):
		return False
	if isOne(s):
		return False
	while not isOne(s):
		if len(s) == 0 or isOdd(s):
			return False
		s = dividedBy2(s)	
	return True
def isOdd(s):
	if int(s[len(s)-1]) % 2 == 1:
		return True
	return False
def isOne(s):
	n = len(s)
	if n == 1 and s[0] == '1':
		return True
	return False
def dividedBy2(s):
	if len(s) == 0:
		return []
	for i in range(len(s)):
		n = int(s[i])
		if n%2 == 0:
			s[i] = str(n/2)
		else:
			s[i] = str(n/2)
			s[i+1] = '1' + s[i+1]
	s = removeZerors(s)
	return s
def removeZerors(s):
	i = 0
	while i < len(s) and s[i] == '0':
		i += 1
	return s[i:]
s = '20'
print Solution(s)