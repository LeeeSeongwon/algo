import sys
from sys import stdin

sys.setrecursionlimit(10000)
input = stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(v):
    visited[v] = True
    for e in graph[v]:
        if visited[e] == False:
            dfs(e)


for i in range(1, n + 1):
    if visited[i] == False:
        dfs(i)
        cnt += 1

print(cnt)
