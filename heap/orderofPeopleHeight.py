# You are given the following :
#
# A positive number N
# Heights : A list of heights of N persons standing in a queue
# Infronts : A list of numbers corresponding to each person (P)
# that gives the number of persons who are taller than P and standing in front of P
# You need to return list of actual order of persons's height
#
# Consider that heights will be unique
#
# Example
#
# Input :
# Heights: 5 3 2 6 1 4
# InFronts: 0 1 2 0 3 2
# Output :
# actual order is: 5 3 2 1 6 4
# So, you can see that for the person with height 5, there is no one taller than
# him who is in front of him, and hence Infronts has 0 for him.
#
# For person with height 3, there is 1 person ( Height : 5 ) in front of him who is taller than him.
class Node:
	def __init__(self,person):
		self.person = person
		self.left = None
		self.right = None
		self.value = 0
class Person:
	def __init__(self,height,infront):
		self.infront = infront
		self.height = height
def order(height,infront):
	persons = [0]*len(height)
	for i in range(len(height)):
		persons[i] = Person(height[i],infront[i])
	persons.sort(key = lambda x: x.height,reverse = True )
	root = Node(persons[0])
	for i in range(1,len(height)):
		insert(root,persons[i],persons[i].infront)
	result = []
	inorderTraverse(root,result)
	return result
def insert(root,person,infront):
	if root is None:
		return Node(person)
	if root.value >  infront:
		root.left =	insert(root.left,person,infront)
		root.value += 1
	else:
		root.right = insert(root.right,person,infront-root.value)
	return root
def inorderTraverse(root,result):
	if root is None:
		return
	inorderTraverse(root.left,result)
	result.append(root.person.height)
	inorderTraverse(root.right,result)
height = [5, 3, 2, 6, 1, 4]
infront = [0, 1, 2, 0, 3, 2]
print order(height,infront)
