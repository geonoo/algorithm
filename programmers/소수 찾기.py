import itertools


def solution(numbers):
    answer = 0
    lst = list(map(int, numbers[::]))
    print(list(itertools.combinations(lst,)))


    return answer

# def sosoo(n):

print(solution("17"))

# "17"	3
# "011"	2