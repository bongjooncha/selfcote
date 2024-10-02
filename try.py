import sys

n, m , v = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

tf1 = [False] * (n+1)
tf2 = tf1[:]
dfs_ans = []
bfs_ans = []

def dfs(graph, v, tf):
    tf[v] = True
    global dfs_ans
    dfs_ans.append(v)

    for i in graph[v]:
        if tf[i] == False:
            dfs(graph,i,tf)

dfs(graph, v, tf1)
print(*dfs_ans, sep=' ')

from collections import deque

def bfs(graph, v, tf):
    que = deque([v])
    tf[v] = True

    global bfs_ans

    while que:
        a = que.popleft()
        bfs_ans.append(a)

        for i in graph[a]:
            if tf[i] == False:
                que.append(i)
                tf[i] = True
bfs(graph, v, tf2)
print(*bfs_ans)
    