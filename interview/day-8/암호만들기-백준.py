# 암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
# 새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다.

# 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다. -> sort
# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. -> if

import itertools
import sys

L, C = map(int, sys.stdin.readline().split(' '))
m = sorted((sys.stdin.readline().strip().split(' ')))
print(m)
comb = list(itertools.combinations(m, L))
moeum = set(['a', 'e', 'i', 'o', 'u'])




for c in comb:
    moeumLen = len(moeum & set(c))
    if moeumLen >= 1 and L - moeumLen >= 2:
        print(''.join(c))


# acis
# acit
# aciw
# acst
# acsw
# actw
# aist
# aisw
# aitw
# astw
# cist
# cisw
# citw
# istw