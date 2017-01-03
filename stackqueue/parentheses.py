def isValid(A):
    if len(A) == 0:
        return 1
    if len(A) == 1:
        return 0
    stack = []
    for i in A:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        else:
            if len(stack) == 0:
                return 0
            if (stack[-1] == '(' and i == ')') or (stack[-1] == '{' and i == '}') or (stack[-1] == '[' and i == ']'):
                stack.pop()
            else:
                return 0
    if len(stack) == 0:
        return 1
    return 0
s = '()[]'
print isValid(s)