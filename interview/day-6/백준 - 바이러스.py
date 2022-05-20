from sys import stdin
read = stdin.readline
dic={}
for i in range(int(read())):
    dic[i+1] = set()
for j in range(int(read())):
    a, b = map(int,read().split())
    dic[a].add(b)
    dic[b].add(a)

print(dic)

def dfs(start):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i)
visited = []
dfs(1)
print(len(visited)-1)
