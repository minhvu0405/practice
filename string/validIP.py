
def Solution(s):
	if len(s) < 4 or len(s) > 12:
		return []
	validIP = []
	for i in [1,2,3]:
		for j in [i+1,i+2,i+3]:
			for k in [j+1,j+2,j+3]:
				if len(s) - k > 3 or len(s) - k < 1:
					continue
				if checkValid(s[:i]) and checkValid(s[i:j]) and checkValid(s[j:k]) and checkValid(s[k:]):
					validIP.append(s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:])
	return sorted(validIP)
def checkValid(number):
	if number[0] == "0" and number != "0":
		return False
	if 0 <= int(number) <= 255:
		return True
	return False
# print Solution('25525511135')
a = Solution('111101')
print sorted(a)