# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
def Solution(s):
	s = stripString(s)
	print s
	for i in range(len(s)/2):
		if s[i] != s[len(s)-1-i]:
			return 0
	return 1
def stripString(s):
	a = ""
	for i in s:
		if i.isdigit() or i.isalpha():
			a += i
	return a.lower()
s = "A man, a plan, a canal: Panama"
s2 = "race a car"
s3 = "1a2"
s4 = "1221"
print Solution(s4)