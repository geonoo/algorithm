#jewels는 보석이며, stones은 갖고 있는 돌이다. stones에는 보석이 몇 개나 있을까? 대소문자는 구분한다.
# 가지고 있는 돌이있는데, 그 안에서 보석이 몇 개나 포함되는지 구하는 문제

# 리트코드에 있는 제한사항
# 1 <= jewels.length, stones.length <= 50 -> 보석의 길이가 1 이상, 돌의 길이는 50 이하
# jewels and stones consist of only English letters. -> 보석과 돌은 영문으로 되어 있음
# All the characters of jewels are unique. -> 보석은 유니크함 ( 중복되는 문자가 없다 ) 26+26 = 52


import collections
import time

# 처음 시도해본것
def numJewelsInStones1(jewels: str, stones: str) -> int:
    cnt = 0
    # 돌에있는 값들로 for문을 돌릴건데
    for s in stones:
        # 값중에 보석안에 존재하는 값이면 카운팅
        if s in jewels:
            cnt+=1

    return cnt

# jewels = "aA"
# stones = "aAAbbbb"
# print(numJewelsInStones1(jewels, stones))
# 리트코드에 제출 했을 때, 36 ms	13.9 MB


# 딕셔너리 이용한 풀이
def numJewelsInStones2(jewels: str, stones: str) -> int:
    freqs = {}
    count = 0

    # 돌에 있는 값을 하나씩 꺼내서 딕셔너리에 담아서 빈도수를 계산
    for s in stones:
        if s not in freqs:
            freqs[s] = 1
        else:
            freqs[s] += 1

    # freqs = {'a': 1, 'A': 2, 'b': 4}

    for j in jewels:
        if j in freqs:
            # 보석에서 뽑은 값을 키로 딕셔너리에있는 빈도수 값을 더해줘서 구하는 문제
            count += freqs[j]

    return count

# jewels = "aA"
# stones = "aAAbbbb"
# print(numJewelsInStones2(jewels, stones))
#리트코드에 제출 했을 때, 55 ms	13.9 MB


# defaultdict를 이용한 비교 생략
def numJewelsInStones3(jewels: str, stones: str) -> int:
    freqs = collections.defaultdict(int)
    count = 0

    # 조건절 없이 빈도 수 계산
    for s in stones:
        freqs[s] += 1

    # freqs = {'a': 1, 'A': 2, 'b': 4}

    for j in jewels:
        if j in freqs:
            count += freqs[j]

    return count

# jewels = "aA"
# stones = "aAAbbbb"
# print(numJewelsInStones3(jewels, stones))
##리트코드에 제출 했을 때, 60ms	13.8MB


# 파이썬 다운 방식
def numJewelsInStones4(jewels: str, stones: str) -> int:

    # lst = [s in jewels for s in stones]
    # print(lst)
    # [True, True, True, False, False, False, False]
    return sum(s in jewels for s in stones)

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones4(jewels, stones))

