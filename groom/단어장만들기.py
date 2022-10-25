import sys

n, k = map(int, sys.stdin.readline().strip().split())
arr = []
for _ in range(0,n):
	arr.append(sys.stdin.readline().strip())

arr.sort()

print(sorted(arr, key=lambda x:len(x))[k-1])