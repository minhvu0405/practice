# Given an input string, reverse the string word by word.
# Example:
# Given s = "the sky is blue",
# return "blue is sky the".
def Solution(s):
	word = False
	count = 0
	add = ""
	mylist = []
	index = 0
	for i in range(len(s)):
		if s[i] != " " and word == True:
			count += 1
		elif s[i] != " " and word == False:
			count += 1
			word = True
		elif s[i] == " " and word == True:
			index = i
			word = False
			add += s[i-count:i]
			mylist.append(add)
			add = ""
			count = 0
	add = ""
	for i in range(index,len(s)):
		if s[i] != " ":
			add += s[i]
	if add != "":
		mylist.append(add)
	s = ""
	for i in range(len(mylist)/2):
		mylist[i],mylist[len(mylist)-i-1] = mylist[len(mylist)-i-1],mylist[i]
	for i in range(len(mylist)):
		if i != len(mylist) - 1:
			s += str(mylist[i]) + " "
		else:
			s += str(mylist[i])
	return s
s = "hello world"
print Solution(s)
