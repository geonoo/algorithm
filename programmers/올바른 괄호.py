def solution(s):
    answer = True
    d = {')':'('}
    open = '('
    stack = []

    for i in s:
        if i in open:
            stack.append(i)
        else:
            if not stack:
                return False
            if stack.pop() != d[i]:
                return False
    return not stack

print(solution("(())())"))

# "(())()"
# "()()"