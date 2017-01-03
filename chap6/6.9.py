
def product(number1,number2):
	result = [0]*(len(number1)+len(number2))
	number1 = number1[::-1]
	number2 = number2[::-1]
	for i in range(len(number1)):
		carry = 0
		for j in range(len(number2)):
			value = int(number1[i])*int(number2[j]) + carry
			carry = (result[i+j] + value)/10
			result[i+j] = (result[i+j] + value)%10
		if carry:
			result[i+j+1] += carry
	result.reverse()
	return "".join(str(i) for i in result).lstrip("0") or "0"
print product("99","99")