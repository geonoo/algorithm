import sys
a, b = map(int, sys.stdin.readline().strip().split())
d = int(sys.stdin.readline().strip())

for i in range(1, d+2):
	print(a,b)
	if i % 2 == 1:
		if a % 2 != 0:
			a = a // 2
			b = b + a + 1
		else:
			a = a // 2
			b = b + a
	else:
		if b % 2 != 0:
			b = b // 2
			a = a + b + 1
		else:
			b = b // 2
			a = a + b