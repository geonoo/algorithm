def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i][j]+triangle[i-1][0]
            else:
                triangle[i][j] = triangle[i][j]+max(triangle[i-1][j-1:j+1])
    return max(triangle[-1])


# 00 -> 10
# 00 -> 01

# 10 -> 20
# 10 -> 21

# 11 -> 21
# 11 -> 22


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30