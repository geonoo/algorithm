import heapq
import sys
INF = int(1e9)


def dijkstra_pq(graph, start):
    dist = [INF] * len(graph)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        acc, cur = heapq.heappop(q)
        if dist[cur] < acc:
            continue

        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist


input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

X, K = map(int, input().split())


# 1에서 K 까지의 최단거리
rtn1 = dijkstra_pq(graph, 1)
distanceK = rtn1[K]
# [1000000000, 0, 1, 1, 1, 2]

# K에서 X 까지의 최단거리
rtn2 = dijkstra_pq(graph, K)
distanceX = rtn2[X]
# [1000000000, 2, 2, 1, 1, 0]

# 1~K까지의 최단거리 + K~X까지의 최단거리
distance = distanceK+distanceX
if distance >= INF:
    print(-1)
else:
    print(distance)



