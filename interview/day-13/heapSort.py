import heapq

def sorted_by_heap(lst):
    heapq.heapify(lst)
    return [heapq.heappop(lst) for _ in range(len(lst))]


print(sorted_by_heap([5,7,9,3,2,1,6,8,9,0,6,4,3,2,6,1]))