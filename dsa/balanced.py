def is_balanced(string):
    stack = []
    bracket_map = {')':'(',']':'[','}':'{'}
    for char in string:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else :
                return 'Not Balanced'
    return 'Not Balanced' if stack else 'Balanced'

print(is_balanced('({[]})'))
print(is_balanced('({[]]})'))
print(is_balanced('({[[hello]]]})'))
print(is_balanced('({[[hello]]})'))

