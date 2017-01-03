
def move(p,U):
	q = []
	for i in range(len(p)):
		s = p[(i-U)%len(p)]
		q.append(s)
	return q
p = [2,1,4,0,0]
print move(p,1)