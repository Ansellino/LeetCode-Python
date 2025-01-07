def superReducedString(s):
    # Write your code here
    stack = []
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    
    if len(stack)>0:
        return ''.join(stack)
    else:
        return "Empty String"