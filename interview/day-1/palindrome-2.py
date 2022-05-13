import re
import time


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


start = time.time()
print(isPalindrome('A man, a plan, a canal: Panama'))
end = time.time()
print(f"{end - start:.8f} sec")
