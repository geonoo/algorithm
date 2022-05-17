def isValid(s: str) -> bool:

    if len(s) % 2 != 0:
        return False

    default = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    open = '({['
    stack = []
    for i in s:
        if i in open:
            stack.append(i)
        else:
            if not stack:
                return False
            if default.get(i) != stack.pop():
                return False

    return not stack

print(isValid("(){}[]"))




def isValid2(s: str) -> bool:
    stack = []
    default = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    open = "([{"
    for char in s:
        if char in open:
            stack.append(char)
        else:
            if not stack:
                return False
            if stack.pop() != default[char]:
                return False

    return not stack

print(isValid2("(){}[]"))


# Input: s = "()"
# Input: s = "()[]{}"
# Input: s = "(]"
