# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	[2,5,7,9,12]
import itertools


def solution(numbers):
    sets = set()
    comb = list(itertools.combinations(numbers, 2))
    for i in comb:
        sets.add(i[0]+i[1])

    return sorted(sets)

print(solution([2,1,3,4,1]))