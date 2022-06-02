# B[P[i]] = A[i]
# 3
# 2 3 1
#
# 1 2 0
import collections
import sys

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().strip().split()))
# B = sorted(A)
# C = collections.defaultdict(collections.deque)
# for i in range(N):
#     C[B[i]] += [i]
# arr = []
# for i in range(N):
#     arr.append(C[A[i]].popleft())
# print(' '.join(map(str,arr)))


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
B = sorted(A)
ans = []
for i in A:
    idx = B.index(i)
    ans.append(idx)
    B[idx] = -1
print(ans)
