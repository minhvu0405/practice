# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# Example:
# if n = 2,
# the sequence is 11.
def Solution(n):
	s = "1"
	k = 1
	while k < n:
		temp = s[0]
		string = ""
		count = 0
		for i in range(len(s)):
			if temp == s[i]:
				count += 1
			else:
				string += str(count) + temp
				temp = s[i]
				count = 1
		string += str(count) + temp
		k += 1
		s = string
	return s
print Solution(7)