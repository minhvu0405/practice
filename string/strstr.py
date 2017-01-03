# Implement strStr().
#  strstr - locate a substring ( needle ) in a string ( haystack ).
def Solution(pattern,text):		#Brute force
	if len(pattern) == 0 or len(text) == 0:
		return -1
	for i in range(len(text)):
		for j in range(len(pattern)):
			if i+j < len(text) and pattern[j] != text[i+j]:
				break
			if i+j >= len(text):
				break
			if j == len(pattern) - 1:
				return i
	return -1
pattern = "baba"
text = "bbbbbbbbab"
print Solution(pattern,text)