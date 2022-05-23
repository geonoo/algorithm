import sys
sys.setrecursionlimit(10**6)
#python이 정한 최대 재귀 깊이는 sys.getrecursionlimit()을 이용해 확인할 수 있다.
# BOJ의 채점 서버에서 이 값은 1,000으로 되어 있다.
# 횟수가 이 값을 넘으면 ReferenceError가 뜬다.

#sys.setrecursionlimit()을 사용하면 Python이 정한 최대 재귀 깊이를 변경할 수 있다.
#문제의 입력값을 보고 재귀가 얼마나 일어날지 가늠하여 깊이를 변경해주면 된다.
# 이 문제에서는 n이 최대 100,000이므로 넉넉히 sys.setrecursionlimit(10**6)으로 설정하니 정답 판정을 받을 수 있었다.
input = sys.stdin.readline

N = int(input())
Tree = [[] for _ in range(N+1)]
Parent = [0 for _ in range(N+1)]

# 그래프의 연결 상태만 표시하는 2차원 배열
for _ in range(N-1):
    a, b = map(int, input().split(' '))
    Tree[a].append(b)
    Tree[b].append(a)

# print(Tree)

def dfs(start):
    for i in Tree[start]:
        # 첫 방문일 때만 dfs
        if Parent[i] == 0:
            # 방문한 값 부모 리스트에 넣기
            Parent[i] = start
            # 다음 노드 찾기
            dfs(i)

dfs(1)
# 1번 노드를 제외한 다음 노드 부터 부모 찾기
for i in range(2, len(Parent)):
    print(Parent[i])
