
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# Example :
#
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
def decode_rec(s):
	if len(s) <= 1:
		return 1
	count = 0
	if s[-1] > '0':
		count = decode_rec(s[:-1])
	if s[-2] < '2' or (s[-2] == '2' and s[-1] < '7'):
		count += decode_rec(s[:-2])
	return count
def decode(s):
	if len(s) <= 1:
		return 1
	table = [0]*(len(s)+1)
	table[0] = 1
	table[1] = 1
	for i in range(2,len(s)+1):
		if s[-1] > '0':
			table[i] = table[i-1]
		if s[-2] < '2' or (s[-2] == '2' and s[-1] < '7'):
			table[i] += table[i-2]
	return table
print decode_rec('121')
print decode('121')
				
	
