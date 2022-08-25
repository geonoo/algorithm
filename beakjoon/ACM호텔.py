import sys

for _ in range(int(sys.stdin.readline())):

    h, w, n = map(int, sys.stdin.readline().strip().split())

    high = 0
    width = 0
    if n % h == 0:
        high = h * 100
        width = n // h
        
    # if (n % h == 0) {
    # hh = h * 100;
    # ww = n / h;
    # } else {
    # hh = n % h * 100;
    # ww = n / h+1;
    # }
    # System.out.println(hh + ww);


# 2
# 6 12 10
# 30 50 72