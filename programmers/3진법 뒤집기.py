
# + 는 더하기
# - 는 빼기
# * 는 곱하기
# / 는 나누기
# % 는 나머지
# // 는 몫
# ** 는 거듭제곱

# divmod 몫과 나머지를 동시에
def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return int(rev_base,3)

print(solution(45))