import sys

n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs_ans = []
bfs_ans = []
tf1 = [False]*(n+1)
tf2 = tf1[:]

def dfs(graph, v, tf):
    tf[v] = True
    global dfs_ans
    dfs_ans.append(v)
    for i in graph[v]:
        if tf[i] is False:
            dfs(graph,i,tf)

from collections import deque
def bfs(graph, v, tf):
    que = deque([v])
    global bfs_ans
    bfs_ans.append(v)
    tf[v]=True
    while que:
        a = que.popleft()
        for i in graph[a]:
            if tf[i] is False:
                que.append(i)
                bfs_ans.append(i)
                tf[i] = True

dfs(graph,v,tf1)
bfs(graph,v,tf2)

print(*dfs_ans)
print(*bfs_ans)
