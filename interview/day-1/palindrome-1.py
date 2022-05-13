import collections
import math
import time
from typing import Deque


def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    print(strs)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

start = time.time()
print(isPalindrome('A man, a plan, a canal: Panama'))
end = time.time()
print(f"{end - start:.5f} sec")

def isPalindrome(s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True

start = time.time()
print(isPalindrome('A man, a plan, a canal: Panama'))
end = time.time()
print(f"{end - start:.5f} sec")



