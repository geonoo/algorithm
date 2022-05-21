import collections
from typing import List


def findItinerary(tickets: List[List[str]]) -> List[str]:
    visited = []
    def dfs(start, t):
        visited.append(start)

        for i in t:
            if i[0] == visited[-1]:
                s = i[1]
                t.remove(i)
                dfs(s, t)

    dfs('JFK', sorted(tickets))
    return visited


def findItinerary2(tickets: List[List[str]]) -> List[str]:
    tic = collections.defaultdict(list)
    for a,b in sorted(tickets, reverse=True):
        tic[a].append(b)

    visited = []
    def dfs(start):
        while tic[start]:
            dfs(tic[start].pop())
        visited.append(start)


    dfs('JFK')
    return visited[::-1]

# Input
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output
# ["JFK","SFO","ATL","JFK","ATL","SFO"]
# Expected
#["JFK","ATL","JFK","SFO","ATL","SFO"]

t = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(t))

#["JFK ","MUC","LHR","SFO","SJC"]