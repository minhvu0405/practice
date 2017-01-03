def reverseSentence(s):
	s = stripSpaces(s)
	array = list(s)
	reverse(array,0,len(array)-1)
	start = 0
	for i in range(len(array)):
		if array[i] == " ":
			reverse(array,start,i-1)
			start = i+1
	reverse(array,start,len(array)-1)
	return "".join(array)
def stripSpaces(s):
	array = list(s)
	if array is None:
		return ""
	result = []
	for i in range(len(s)):
		if array[i] != " ":
			result.append(array[i])
		elif array[i] == " " and array[i-1] and array[i-1] != " ":
			result.append(array[i])
	if result[-1] ==  " ":
		result.pop()
	return "".join(result)
def reverse(array,start,end):
	if array is None:
		return
	while start < end:
		array[start],array[end] = array[end],array[start]
		start += 1
		end -= 1

s = " this is my test "
print reverseSentence(s)
