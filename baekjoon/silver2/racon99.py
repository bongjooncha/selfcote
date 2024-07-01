# https://www.acmicpc.net/problem/18126
import sys
sys.setrecursionlimit(10**9)

N=int(input())
graphs = [list(map(int, input().split())) for _ in range(N-1)]
Tree=[ [] for _ in range(N+1) ]

[Tree[a].append((b, c)) for a, b, c in graphs]
[Tree[b].append((a, c)) for a, b, c in graphs]

visited = [0] * (N+1)

# graph: (목적지, 거리), v:시작점
def dfs(graph, v):
        for end, distance in graph[v]:
            if visited[end] is 0 and end is not 1:
                visited[end] = visited[v] + distance
                dfs(graph, end)
                
dfs(Tree,1)
print(max(visited))

# 9
# 1 2 1
# 1 3 1
# 4 2 1
# 2 5 1
# 4 6 1
# 4 7 1
# 7 8 1
# 3 9 1

# 4
# 1 4 1
# 1 2 1
# 4 3 1