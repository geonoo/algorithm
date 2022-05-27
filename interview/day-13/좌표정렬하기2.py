import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
rtn = []
for _ in range(N):
    rtn.append(list(map(int, sys.stdin.readline().strip().split(' '))))

def compare(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1] and a[0] < b[0]:
        return -1
    else:
        return 0
for i in sorted(rtn, key=cmp_to_key(compare)):
    print(' '.join(map(str, i)))


# 1 -1
# 1 2
# 2 2
# 3 3
# 0 4