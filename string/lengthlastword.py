# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.
def Solution(s):
	if len(s) < 1:
		return 0
	count = 0
	for i in range(len(s)):
		if s[i] != " ":
			count += 1
		elif s[i] == " " and i+1 < len(s):
			if s[i+1] != " ":
				count = 0
	return count

s = " Hello "
print Solution(s)
