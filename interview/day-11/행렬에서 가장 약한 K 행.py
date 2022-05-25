import collections
import heapq
from typing import List


def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    ans = []
    s = collections.defaultdict(int)
    for i in range(len(mat)):
        c = collections.Counter(mat[i])
        s[i] = c[1]

    s = sorted(s.items(), key=lambda x:x[1])
    for key, val in s:
        ans.append(key)

    return ans[:k]

def kWeakestRows2(mat: List[List[int]], k: int) -> List[int]:
    heap = []
    answer = []
    for i in range(len(mat)):
        cnt = mat[i].count(1)
        heapq.heappush(heap, [cnt, i])
    for _ in range(k):
        answer.append(heapq.heappop(heap)[1])

    return answer


def kWeakestRows3(mat: List[List[int]], k: int) -> List[int]:
    s = collections.defaultdict(int)
    for i in range(len(mat)):
        c = collections.Counter(mat[i])
        s[i] = c[1]

    ss = sorted(s.items(),key=lambda x:x[1])

    ans = []
    for i in range(k):
        ans.append(ss[i][0])

    return ans

print(kWeakestRows2([
     [1, 1, 0, 0, 0],
     [1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1]],3))

# 3 -> idx [2,0,3]
# [
#      [1, 1, 0, 0, 0],
#      [1, 1, 1, 1, 0],
#      [1, 0, 0, 0, 0],
#      [1, 1, 0, 0, 0],
#      [1, 1, 1, 1, 1]
# ]



