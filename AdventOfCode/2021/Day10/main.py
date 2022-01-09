
def is_open_bracket(char):
    return char == '(' or char == '[' or char == '{' or char == '<'

def is_closing_bracket(opened, closed):
    if opened == '(' and closed == ')':
        return True
    if opened == '<' and closed == '>':
        return True
    if opened == '[' and closed == ']':
        return True
    if opened == '{' and closed == '}':
        return True
    
    return False

def bracket_to_score(char):
    if char == '(':
        return 1
    if char == '[':
        return 2
    if char == '{':
        return 3
    if char == '<':
        return 4

file = open('file.txt')

score = {')': 0, '}': 0, '>': 0, ']': 0}
points = []
for line in file.readlines():
    stack = []
    
    for char in line.rstrip():
        if is_open_bracket(char):
            stack.append(char)
        elif is_closing_bracket(stack[-1], char):
            stack.pop()
        else:
            #score[char] += 1
            break
    else:
        p = 0
        for _ in range(0, len(stack)):
            p = (p * 5) + bracket_to_score(stack[-1])
            stack.pop()
        points.append(p)
    
points = sorted(points)
print(points[len(points)//2])