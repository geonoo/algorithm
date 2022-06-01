import heapq
import sys

INF = int(1e9)
def dijkstra(graph, start):
    dist = [INF]*len(graph)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        val, idx = heapq.heappop(q)
        if dist[idx] < val:
            continue
        for idx2, val2 in graph[idx]:
            cost = val + val2
            if cost < dist[idx2]:
                dist[idx2] = cost
                heapq.heappush(q, (cost, idx2))
    return dist


input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

rtn = dijkstra(graph, start)
for r in rtn[1:]:
    if r >= INF:
        print('INF')
    else:
        print(r)