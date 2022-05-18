import collections
import heapq
from typing import List



def topKFrequent1(nums: List[int], k: int) -> List[int]:
    count = list(collections.Counter(nums).most_common(k)) # k 이상의 최빈값
    rtn = []
    for i in range(len(count)):
        rtn.append(count[i][0])

    return rtn

def topKFrequent2(nums: List[int], k: int) -> List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    for f in freqs:
        heapq.heappush(freqs_heap,(-freqs[f], f))

    topk = list()
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

def topKFrequent3(nums: List[int], k: int) -> List[int]:
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


print(topKFrequent3([1,1,1,2,2,3], 2))
# [1,1,1,2,2,3], 2
# [3,0,1,0], 1