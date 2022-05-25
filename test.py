import heapq

heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heapq.nlargest(2,heap))
print(heapq.nsmallest(2,heap))

#[1, 3, 5, 4, 8, 7]