def search(text,pattern):
	for i in range(len(text)-len(pattern)+1):
		found = True
		for j in range(len(pattern)):
			if text[i+j] != pattern[j]:
				found = False
				break
		if found:
			return i
	return -1
text = "this is a test"
pattern = "test"
print search(text,pattern)
