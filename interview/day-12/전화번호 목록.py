import sys

def start_number(l):
    for i, j in zip(l, l[1::]):
        if j.startswith(i):
            return 'NO'
    return 'YES'


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    lst = [str(sys.stdin.readline().strip()) for _ in range(n)]
    print(start_number(sorted(lst)))


