case = int(input())
for p in range(case):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    queue = []
    for i, j in enumerate(nums):
        queue.append((i, j))

    rank = 0

    while len(queue) > 0:
        high = max(queue, key=lambda x: x[1])[1]
        if queue[0][1] == high:
            a = queue.pop(0)
            rank += 1
            if a[0] == M:
                print(rank)
                break
        else:
            while queue[0][1] != high:
                queue.append(queue.pop(0))