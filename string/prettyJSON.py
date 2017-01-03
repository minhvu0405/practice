# Pretty print a json object using proper indentation.
#     Every inner brace should increase one indentation to the following lines.
#     Every close brace should decrease one indentation to the same line and the following lines.
#     The indents can be increased with an additional '\t'

def prettyJSON(s):
	line = ""
	result = []
	indent = ""
	for i in range(len(s)):
		if s[i] == '{' or s[i] == '[':
			if line != "":
				result.append(indent+line)
			result.append(indent+s[i])
			indent += '\t'
			line = ""
		elif s[i] == '}' or s[i] == ']':
			if line != "":
				result.append(indent+line)
			indent = indent[:-1]
			result.append(indent+s[i])
			line = ""
		elif s[i] == ',':
			if s[i-1] == "}" or s[i-1] == ']':
				result[-1] = result[-1] + s[i]
			else:
				result.append(indent+line+s[i])
				line = ""
		elif s[i] != ' ':
			line += s[i]
	return result
# s = '{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
s = '["foo", {"bar":["baz",null,1.0,2]}]'
json = prettyJSON(s)
for i in json:
	print i