import math
import sys

x, y, z = map(int, sys.stdin.readline().strip().split())

print(math.ceil((z-x) / (x-y))+1)

