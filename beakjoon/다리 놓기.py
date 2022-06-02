import sys

T = int(sys.stdin.readline())
for _ in range(T):
    R, N = map(int, sys.stdin.readline().strip().split())
    boonja = 1
    for i in range(N, 1, -1):
        boonja *= i
    boonmo = 1
    for i in range(N-R, 1, -1):
        boonmo *= i
    r = 1
    for i in range(R, 1, -1):
        r *= i
    print(boonja//(boonmo*r))
