# Given a roman numeral, convert it to an integer.
def Solution(s):
	dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
	if len(s) < 1:
		return 0
	i = 0
	num = 0
	while i < len(s):
		if s[i] in dic:
			if i + 1 < len(s) and ((s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")) or (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M"))) :
				num += dic[s[i+1]] - dic[s[i]]
				i += 2
			else:
				num += dic[s[i]]
				i += 1
		else:
			return num
	return num
print Solution("MCMIV")
print Solution("MMXIV")
print Solution("MCMXC")
print Solution("MCMLIV")
print Solution("")
print Solution("XAX")