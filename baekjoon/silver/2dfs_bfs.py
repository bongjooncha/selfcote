# https://www.acmicpc.net/problem/1260

n, r, s = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(r):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited1 = [False]*(n+1)
visited2 = [False]*(n+1)

dfs_ans = []
def dfs(map, v, visited):
    if visited[v] == False:
        visited[v] = True
    global dfs_ans
    dfs_ans.append(v)

    for i in map[v]:
        if not visited[i]:
            dfs(graph,i,visited)

bfs_ans = []
from collections import deque

def bfs(map,v,visited):
    que = deque([v])

    if visited[v] == False:
        visited[v] = True
    global bfs_ans
    while que:
        i = que.popleft()
        bfs_ans.append(i)
        
        for j in map[i]:
            if not visited[j]:
                que.append(j)
                visited[j] = True

dfs(graph, s, visited1)
bfs(graph, s, visited2)
print(*dfs_ans, sep=' ')
print(*bfs_ans, sep=' ')