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
    for i in range(len(mat)):
        # 1의 개수
        soldiers = mat[i].count(1)
        heapq.heappush(heap, [soldiers, i])

    answer = []
    for i in range(k):
        answer.append(heapq.nsmallest(k, heap)[i][1])

    return answer



print(kWeakestRows2([
     [1, 1, 0, 0, 0],
     [1, 1, 1, 1, 0],
     [1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 1, 1, 1, 1]],3))