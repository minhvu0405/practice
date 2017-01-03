def replace_remove(s):
	if s == "":
		return ""
	array = list(s)
	lenWrite = 0
	count_a = 0
	for i in range(len(array)):
		if array[i] != "b":
			array[lenWrite] = array[i]
			lenWrite += 1
	l = lenWrite-1
	for i in range(lenWrite-1,-1,-1):
		if array[i] != "a":
			array[l] = array[i]
		else:
			array[l] = "dd"
		l -= 1
	return "".join(array[:lenWrite])
print replace_remove("abcd")