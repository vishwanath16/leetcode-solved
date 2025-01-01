# Link: https://leetcode.com/problems/valid-parentheses/description/


def isValid(s):

    sets = {')': '(', '}': '{', ']': '['}

    stack = []

    for c in s:
        if c in sets:
            if stack and stack[-1] == sets[c]:
                stack.pop()
            else:
                return False 
        else:
            stack.append(c)
    
    return not stack

print(isValid('()[]{}'))