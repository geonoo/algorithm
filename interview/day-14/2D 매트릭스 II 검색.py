import bisect
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:

    for i in range(len(matrix)):
        j = bisect.bisect_left(matrix[i], target)
        if j < len(matrix[i]) and matrix[i][j] == target:
            return True
    return False



print(searchMatrix([[-1,3]],3))

# Input: matrix = [
#                   [1,4,7,11,15],
#                   [2,5,8,12,19],
#                   [3,6,9,16,22],
#                   [10,13,14,17,24],
#                   [18,21,23,26,30]]

# target = 5
# Output: true