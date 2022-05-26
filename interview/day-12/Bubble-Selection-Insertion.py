def bubble(lst):

    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

# print(bubble([4, 6, 2, 9, 1]))



def selection(lst):

    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if lst[min] > lst[j]:
                min = j
        if min != i:
            lst[min], lst[i] = lst[i], lst[min]

    return lst

print(selection([4, 6, 2, 9, 1]))

def insertion(lst):
    for i in range(1, len(lst)):
        for j in range(1, i+1):
            cur = i-j
            if lst[cur] > lst[cur+1]:
                lst[cur], lst[cur+1] = lst[cur+1], lst[cur]
            else:
                break

    return lst

# print(insertion([4, 6, 2, 9, 1]))