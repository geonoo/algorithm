import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
lst = set([sys.stdin.readline().strip() for _ in range(N)])

def compare(a, b):
    if len(a) < len(b):
        return -1
    elif len(a) == len(b) and a < b:
        return -1
    else:
        return 0

for l in sorted(lst, key=cmp_to_key(compare)):
    print(l)