# Given an absolute path for a file (Unix-style), simplify it.
def split(A):
	l = []
	s = ""
	for i in range(len(A)):
		if A[i] != '/':
			s += A[i]
		else:
			if s != "":
				l.append(s)
				s = ""
	if len(s) != 0:
		l.append(s)
	return l
def join(l):
	s = ""
	for i in l:
		s += "/" + str(i) + "/"
	return s
def simplifyPath(A):
	if len(A) == 0:
		return "/"
	l = split(A)
	stack = []
	for i in l:
		if i == "..":
			if len(stack) != 0:
				stack.pop()
		elif i != ".":
			stack.append(i)
	return join(stack)
s = "/a/../home/minh/"
print simplifyPath(s)
k = "/a//h/c/../d/e/"
print simplifyPath(k)
t = "/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/.."
print simplifyPath(t)