def solution(train):
    visited = []
    dfs(train, 0, [])
    answer = -1
    return answer
    
def dfs(arr, cur, visited):
    visited[cur] = True
    for i in arr[cur]:
        if not visited[i]:
            dfs(arr, cur, visited)

#E오, W왼, S아래, N위
print(solution(["EW", "EW", "EW"]))
# ["EW", "EW", "EW"]