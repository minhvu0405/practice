# Implement atoi to convert a string to an integer.
# Input : "9 2704"
# Output : 9
# Input: "-123A 8a35"
# Output: -123
def Solution(s):
	s = getNumbers(s)
	if len(s) < 1:
		return
	negative = False
	if s[0] == "-":
		negative = True
	start = 0
	if negative == True or s[0] == "+":
		start = 1
	num = 0
	for i in range(start,len(s)):
		if not ("0" <= s[i] <= "9"):
			if negative == True:
				return -num
			else:
				return num
		else:
			num = num*10 + ord(s[i]) - ord('0')
			if num > 2147483647 and negative == False:
				return 2147483647
			elif num > 2147483647 and negative == True:
				return -2147483648
	if negative == True:
		return -num
	return num
def getNumbers(s):
	number = ""
	flag = False
	for i in range(len(s)):
		if s[i] != " " and flag == True:
			number += s[i]
		elif s[i] != " " and flag == False:
			flag = True
			number += s[i]
		elif s[i] == " " and flag == True:
			break
	return number
print Solution("-12390A 8a35")