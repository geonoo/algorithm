import collections
from typing import List


def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    print(graph)
    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False

        # 이미 방문했던 노드이면
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)
        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True


print(canFinish(2, [[0,1],[0,2],[1,2]]))
# numCourses = 2, prerequisites = [[1, 0]]
# Ture
# numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# False

