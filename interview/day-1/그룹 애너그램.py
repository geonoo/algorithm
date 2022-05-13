import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # 존재하지 않는 키를 삽입하려고 하면 keyError가 나서 defaultdict
    anagrams = collections.defaultdict(list)
    for word in strs:
        # 알파벳 순으로 정렬한 문자열을 ss에 담는다.
        ss = ''.join(sorted(word))
        # 알파벳 순으로 정렬된 문자열을 키로 원래 문자열을 담아준다.
        anagrams[ss].append(word)
        # 키를 제외한 리스트 값만 리스트에 담아서 반환해준다.
    return list(anagrams.values())

print(groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    val = collections.defaultdict(list)

    for word in strs:
        ss = ''.join(sorted(word))
        val[ss].append(word)

    return list(val.values())


print(groupAnagrams2(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
