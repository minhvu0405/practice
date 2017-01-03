# Given a text and a pattern, write a function to print all occurences of pattern in text.
import string
def search_BF(text,pattern):
	if len(text) < len(pattern):
		return
	result = []
	for i in range(len(text)):
		for j in range(len(pattern)):
			if i + len(pattern) - 1 >= len(text):
				break
			if pattern[j] != text[i+j]:
				break
			if j == len(pattern) - 1:
				result.append(i) 
	return result
def search_hash(text,pattern):
	if len(text) < len(pattern):
		return
	hashSum = sum([hash(i) for i in pattern])
	lenPattern = len(pattern)
	result = []
	s = 0
	count = 0
	for i in range(len(text)):
		s += hash(text[i])
		count += 1
		if count == lenPattern:
			if s == hashSum:
				result.append(i-lenPattern+1)
			count -= 1
			s -= hash(text[i - lenPattern + 1])
	return result
text = "The average case and best case running time of the Rabin-Karp algorithm is O(n+m)"
pattern = "case"
print search_BF(text,pattern)
print search_hash(text,pattern)