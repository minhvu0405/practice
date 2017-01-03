# Given two numbers represented as strings, return multiplication of the numbers as a string.
def multiply(s1,s2):	# 10**i is slow
	s1 = s1[::-1]
	s2 = s2[::-1]
	result = 0
	for i in range(len(s2)):
		carry = 0
		t = 0
		for j in range(len(s1)):
			n = int(s1[j])*int(s2[i]) + carry
			carry = n/10
			t += (n%10)*(10**j)
		if carry != 0:
			t += carry*(10**len(s1))
		result += t*(10**i)
	return str(result)
def Solution(s1,s2):		
	s1 = s1[::-1]
	s2 = s2[::-1]
	s = [0]*(len(s1)+len(s2))
	for i in range(len(s2)):
		carry = 0
		for j in range(len(s1)):
			n = int(s1[j])*int(s2[i]) + carry + s[i+j]
			carry = n/10
			s[i+j] = n%10
		if carry != 0:
			s[i+j+1] += carry
	s = s[::-1]
	result = ""
	i = 0
	flag = False
	while i < len(s):
		if s[i] != 0 and flag == False:
			result += str(s[i])
			flag = True
		elif flag == True:
			result += str(s[i])
		i += 1
	if result == "":
		result = '0'
	return result 
s1 = "99"
s2 = "0"
print Solution(s1,s2)