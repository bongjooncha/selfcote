# https://www.acmicpc.net/problem/1260

import sys
n, m, v = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

v1 = [False]*(n+1)
v2 = v1[:]

dfs_ans = []
def dfs(graph, v, visits):
    visits[v] = True
    global dfs_ans
    dfs_ans.append(v)

    for i in graph[v]:
        if not visits[i]:
            dfs(graph,i,visits)

from collections import deque
bfs_ans = []

def bfs(graph, v, visits):
    que = deque([v])
    visits[v] = True
    
    global bfs_ans
    while que:
        a = que.popleft()
        bfs_ans.append(a)

        for i in graph[a]:
            if not visits[i]:
                que.append(i)
                visits[i] = True

dfs(graph, v, v1)
print(*dfs_ans, sep=' ')
bfs(graph, v, v2)
print(*bfs_ans, sep=' ')