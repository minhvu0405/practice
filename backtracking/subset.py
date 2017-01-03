def Solve(sofar,rest,result):
	if not rest:
		result.append(sofar)
		return
	else:
		Solve(sofar+[rest[0]],rest[1:],result)
		Solve(sofar,rest[1:],result)
result = []
Solve([],[1,2,3],result)
print sorted(result)