# Given a digit string, return all possible letter combinations that the number could represent.
def phoneNumber(digits):
	result = []
	Solve(digits,0,result,[])
	return result
def Solve(digits,step,result,temp):
	if step == len(digits):
		result.append("".join(temp))
		return
	key = {'0': "0", '1': "1", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
	curr = key[digits[step]]
	for i in curr:
		temp.append(i)
		Solve(digits,step+1,result,temp)
		temp.pop()
digits = "234"
print phoneNumber(digits)

