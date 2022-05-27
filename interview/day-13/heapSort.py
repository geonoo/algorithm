def sorted_by_heap(lst):
    maxheap = BinaryMaxHeap()
    for elem in lst:
        maxheap.insert(elem)

    desc = [maxheap.extract() for _ in range(len(lst))]
    return list(reversed(desc))