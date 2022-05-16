import sys

def isValid(s: str) -> str:

    if len(s) % 2 != 0:
        return 'NO'

    default = {
        ')':'('
    }

    open = '('
    stack = []
    for i in s:
        if i in open:
            stack.append(i)
        else:
            if not stack:
                return 'NO'
            if default.get(i) != stack.pop():
                return 'NO'

    if not stack:
        return 'YES'
    else:
        return 'NO'

n = int(sys.stdin.readline())
# strip \n 지우기
lst=[sys.stdin.readline().strip() for i in range(n)]

answer = ['']*len(lst)
for i, v in enumerate(lst):
    answer[i] = isValid(v)

print('\n'.join(answer))


