import sys

n = int(sys.stdin.readline())
lst=[int(sys.stdin.readline().strip()) for i in range(n)]
stack = []
answer = []

cnt = 1
status = True
for i in range(n):
    while cnt <= lst[0]:
        stack.append(cnt)
        cnt +=1
        answer.append('+')
    if stack[-1] == lst[0]:
        lst.pop(0)
        stack.pop()
        answer.append('-')
    else:
        status = False
        break

if status:
    print('\n'.join(answer))
else:
    print('NO')