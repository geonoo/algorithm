def solution(s):
    try:
        int(s)
    except:
        return False
    return True

print(solution('-123'))