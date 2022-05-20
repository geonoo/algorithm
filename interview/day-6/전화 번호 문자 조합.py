import itertools
from typing import List


def letterCombinations(digits: str) -> List[str]:
    if digits == '': return []

    phone = [[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

    lst = [int(i) for i in digits]
    l = [phone[i-1] for i in lst]
    pro = list(itertools.product(*l))

    return [''.join(i) for i in pro]

def productExam(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


print(letterCombinations('23'))