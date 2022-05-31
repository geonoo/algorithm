import heapq
from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # 그래프 만들기
    adj_list = {i: [] for i in range(n)}
    for frm, to, price in flights:
        adj_list[frm].append((to, price))

    best_visited = [2 ** 31] * n

    prior_queue = [(0, -1, src)]  # weight, steps, node

    while prior_queue:
        cost, steps, node = heapq.heappop(prior_queue)

        if best_visited[node] <= steps:
            continue

        if steps > k:  # 현재 스텝이 k 보다 크면 멈추기
            continue

        if node == dst:  # 원하는 도착지에 도착했을때 해당 금액을 반환
            return cost

        best_visited[node] = steps  # 업데이트

        for neighb, weight in adj_list[node]:
            heapq.heappush(prior_queue, (cost + weight, steps + 1, neighb))

    return -1

print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))

# n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1