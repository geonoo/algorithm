import sys

N = int(sys.stdin.readline())
rtn = []
for i in range(N):
    rtn.append((sys.stdin.readline().strip().split()))


for i in sorted(rtn, key=lambda x:int(x[0])):
    print(' '.join(i))
