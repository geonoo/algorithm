import sys

def isValid(s: str) -> str:

    if len(s) % 2 != 0:
        return 'NO'

    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return 'NO'
            if '(' != stack.pop():
                return 'NO'

    if not stack: return 'YES'
    else: return 'NO'

n = int(sys.stdin.readline())
lst=[sys.stdin.readline().strip() for i in range(n)]

answer = ['']*len(lst)
for i, v in enumerate(lst):
    answer[i] = isValid(v)

print('\n'.join(answer))


