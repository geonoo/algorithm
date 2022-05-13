from typing import List


def reorderLogFiles(logs : List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 람다는 식별자 없이 실행 가능한 함수
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters+digits

list = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 2 3', 'own kit dig']
print(reorderLogFiles(list))