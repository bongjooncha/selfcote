import sys
sys.setrecursionlimit(10**9)

N=int(input())
graphs = [list(map(int, input().split())) for _ in range(N-1)]
Tree=[ [] for _ in range(N+1) ]
[Tree[a].append((b, c)) for a, b, c in graphs]

visited = [0] * (N+1)

def dfs(graph, v):
    for end, distance in graph[v]:
        visited[end] = visited[v] + distance
        dfs(graph, end)
dfs(Tree,1)
print(max(visited))