def Solution(number):
	M = ["","M","MM","MMM"]
	C = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
	X = ["","X","XX","XXX","XC","L","LX","LXX","LXXX","XC"]
	I = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
	return	M[number/1000] + C[(number%1000)/100] + X[(number%100)/10] + I[number%10]
def intToRoman1(num):
    values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
    numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
    res, i = "", 0
    while num:
        res += (num//values[i]) * numerals[i]
        num %= values[i]
        i += 1
    return res

print Solution(1523)
print intToRoman1(16)