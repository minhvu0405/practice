def Solution(s1,s2):
	l1 = split(s1)
	l2 = split(s2)
	if len(l1) == 0 and len(l2) == 0:
		return 0
	if len(l1) > 0 and len(l2) == 0:
		return 1
	if len(l1) == 0 and len(l2) > 0:
		return -1
	i = 0
	j = 0
	while i < len(l1) and j < len(l2):
		if int(l1[i]) > int(l2[j]):
			return 1
		elif int(l1[i]) < int(l2[j]):
			return -1
		i += 1
		j += 1
	if i == len(l1) and j == len(l2):
		return 0
	if i < len(l1):
		for k in range(i,len(l1)):
			if int(l1[k]) > 0:
				return 1
		return 0
	if j < len(l2):
		for n in range(j,len(l2)):
			if int(l2[n]) > 0:
				return -1
		return 0
def split(s):
	l = []
	word = ""
	for i in range(len(s)):
		if s[i] != ".":
			word += s[i]
		else:
			l.append(word)
			word = ""
	if word != "":
		l.append(word)
	return l
s1 = "1.0.6"
s2 = "1.1"
print Solution(s1,s2)