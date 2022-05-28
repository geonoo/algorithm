import sys

N = int(sys.stdin.readline().rstrip())
lst1 = set(list(map(int, sys.stdin.readline().rstrip().split(' '))))
M = int(sys.stdin.readline().rstrip())
lst2 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
for l in lst2:
    if l in lst1:
        print('yes')
    else:
        print('no')




# print(N,M)
# print(lst1, lst2)


