# Given two binary strings, return their sum (also a binary string).
def Solution(s1,s2):
	if len(s1) == 0 and len(s2) ==  0:
		return "0"
	if len(s1) == 0:
		return s2
	if len(s2) == 0:
		return s1
	s1 = s1[::-1]
	s2 = s2[::-1]
	i = 0
	j = 0
	result = ""
	carry = "0"
	while i < len(s1) and j < len(s2):
		n = addBinary(addBinary(s1[i],s2[j]),carry)
		carry = findCarry(s1[i],s2[j],carry)
		result += n
		i += 1
		j += 1
	while i < len(s1):
		n = addBinary(s1[i],carry)
		carry = findCarry(s1[i],carry,"0")
		result += n
		i += 1
	while j < len(s2):
		n = addBinary(s2[j],carry)
		carry = findCarry(s2[j],carry,"0")
		result += n
		j += 1
	if carry == "1":
		result += "1"
	return result[::-1]
def findCarry(s1,s2,carry):
	if s1 == "1" and s2 == "1":
		return "1"
	if carry == "1" and (s1 == "1" or s2 == "1"):
		return "1"
	return "0"
def addBinary(s1,s2):
	if s1 == "0" and s2 == "0":
		return "0"
	if s1 == "1" and s2 == "0":
		return "1"
	if s1 == "0" and s2 == "1":
		return "1"
	if s1 == "1" and s2 == "1":
		return "0"
	return ""
s1 = "110011"
s2 = "111"
s3 = "111010"
print Solution(s1,s2)