import collections
def removeDuplicateLetters(s: str) -> str:
    counter = collections.Counter(s)
    stack = []
    seen = set()

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        # 1. stack 안에 값이 존재하는지
        # 2. char 값보다 스택 top에 있는 값이 크면
        # 3. 스탭 top의 숫자가 0보다 크면
        while(stack and char < stack[-1] and counter[stack[-1]] > 0):
            # char값보다 스택 top에 있는값이 사전상 다음 순서이고,
            # 아직 개수가 남았고 다음에 순서에 와야하기 때문에 스택과 seen에서 제거한다.
            # seen값을 제거하고 stack에 top도 제거한다.
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)



    return ''.join(stack)


# s1 = 'bcabc'
# s2 = 'cbacdcbc'
#
# print(removeDuplicateLetters(s2))

def removeDuplicateLetters2(s: str) -> str:
    counter = collections.Counter(s)
    stack = []
    seen = set()

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue

        while(stack and char < stack[-1] and counter[stack[-1]] > 0):
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)


    return ''.join(stack)


s1 = 'bcabc'
s2 = 'cbacdcbc'

print(removeDuplicateLetters(s2))