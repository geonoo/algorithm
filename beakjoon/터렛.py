# r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다. - 접점 0
# r1 + r2 = d 이면 두 원은 외접한다. - 접점 1
# |r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다. - 접점 2
# |r1 - r2| = d 이면 한 원이 다른 원에 내접한다. - 접점 1
# |r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다. - 접점 0
import math
import sys

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())

    d = math.sqrt((x1-x2)**2+(y1-y2)**2)
    a = abs(r1-r2)
    b = r1+r2
    if d == 0 and r1 == r2:
        print(-1)
    elif b == d or a == d:
        print(1)
    elif a < d < b:
        print(2)
    else:
        print(0)


# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5