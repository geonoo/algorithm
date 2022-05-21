from typing import List


def solveNQueens(n: int) -> List[List[str]]:

    visited = [-1]*n
    ans = []
    def dfs(row):
        if row >= n:
            grid = [['.']*n for _ in range(n)]
            for r, c in enumerate(visited):
                grid[r][c] = 'Q'
            rtn = []
            for g in grid:
                rtn.append(''.join(g))
            ans.append(rtn)
            return

        for col in range(n):
            visited[row] = col
            if is_ok(row):
                dfs(row+1)

    def is_ok(nextRow):
        for row in range(nextRow):
            if visited[row] == visited[nextRow] or nextRow-row == abs(visited[row] - visited[nextRow]):
                return False
        return True

    dfs(0)
    return ans


print(solveNQueens(4))

# Input: n = 4
# Output: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]