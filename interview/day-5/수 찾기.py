import sys

n1 = int(sys.stdin.readline())
lst1=list(map(int, sys.stdin.readline().strip().split(' ')))

n2 = int(sys.stdin.readline())
lst2=list(map(int, sys.stdin.readline().strip().split(' ')))


set1 = set(lst1)
set2 = set(lst2)
set3 = set2 - set1

for i in lst2:
    if i not in set3:
        print(1)
    else:
        print(0)


# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5


# 1
# 1
# 0
# 0
# 1