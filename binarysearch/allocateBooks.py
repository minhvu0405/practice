# N number of books are given.
# The ith book has Pi number of pages.
# You have to allocate books to M number of students so that maximum number of pages alloted to a student is minimum.
# A book will be allocated to exactly one student. Each student has to be allocated atleast one book.
# NOTE: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order.
# Input:
# List of Books M number of students
# Your function should return an integer corresponding to the minimum number.
# Example:
# P : [12, 34, 67, 90]
# M : 2
# Output : 113

def Solution(P,M):
	small = max(P)
	big = sum(P)
	if M > len(P):
		return -1
	while small < big:
		mid = (small+big)/2
		n = findNumStudents(mid,P)
		if n <= M:
			big = mid
		else:
			small = mid + 1
	return small
def findNumStudents(mid,P):
	total = 0
	numStudents = 1
	for i in P:
		total += i
		if total > mid:
			total = i
			numStudents += 1
	return numStudents
P = [12,34,67,90]
M = 2
print Solution(P,M)