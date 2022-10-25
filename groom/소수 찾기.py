import sys
n = int(sys.stdin.readline().strip())
arr = sys.stdin.readline().strip().split()

def primeList(n):ls
    n += 1
    sieve = [False, False] + [True] * (n)
    end = int(n**0.5) + 1
    for i in range(2, end):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
                
    return [i for i in range(n) if sieve[i] == True]
	
chk = primeList(len(arr))

ans = 0
for i in chk:
	ans += int(arr[i-1])
	
print(ans)