import itertools
from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    lst = [i for i in range(1,n+1)]
    return list(itertools.combinations(lst, k))


print(combine(1, 1))