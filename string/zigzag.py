def Solution(s,n):
	if n <= 0:
		return ""
	if n == 1:
		return s
	result = ""
	step = 2*(n-1)
	for i in range(n):
		j = i
		if i == 0 or i == n-1:
			while j < len(s):
				result += s[j]
				j += step 
		else:
			while j < len(s):
				result += s[j]
				j += step - 2*i
				if j < len(s):
					result += s[j]
					j += 2*i
				else:
					break
	return result
# s = "PAYPALISHIRING"
s = "ABCDEF"
n = 6
print Solution(s,n)