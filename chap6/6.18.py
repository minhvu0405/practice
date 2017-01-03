def encode(s):
	result = ""
	if s == "":
		return result
	count = 1
	pattern = s[0]
	for i in range(1,len(s)):
		if s[i] == pattern:
			count += 1
		else:
			result += str(count) + pattern
			pattern = s[i]
			count = 1
	result += str(count) + pattern
	return result
def decode(s):
	result = ""
	if s == "":
		return result
	digit = 0
	for i in range(len(s)):
		if s[i].isdigit():
			digit = int(s[i])
		else:
			for k in range(digit):
				result += s[i]
			digit = 0
	return result
a = encode("aaaabccddd")
print decode(a)