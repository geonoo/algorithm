def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        lst = []
        for j in range(len(arr2[i])):
            lst.append(arr1[i][j]+arr2[i][j])
        answer.append(lst)
    return answer


def sumMatrix(A,B):
    # answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    answer = []
    for a, b in zip(A, B):
        list = []
        for c, d in zip(a, b):
            list.append(c+d)
        answer.append(list)

    return answer

print(sumMatrix([[1],[2]],[[3],[4]]))