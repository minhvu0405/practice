# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
# You will be give 2 arrays X and Y. Each point is represented by (X[i], Y[i])
def Solve(X,Y):
	if len(X) == 1:
		return 1
	final = 0
	for i in range(len(A)-1):
		slope = {}
		samePoint = 0
		sameVertical = 0
		maxPoint = 0 
		for j in range(i+1,len(A)):
			x1,y1 = A[i],B[i]
			x2,y2 = A[j],B[j]
			if x1 == x2 and y1 == y2:
				samePoint += 1
			elif x1 == x2:
				sameVertical += 1
				maxPoint = max(maxPoint,sameVertical)
			else:
				s = (y2-y1)*1.0/(x2-x1)
				if s not in slope:
					slope[s] = 1
				else:
					slope[s] += 1
				maxPoint = max(maxPoint,slope[s])
		final = max(final,maxPoint+same+1)
	return final
