# https://www.acmicpc.net/problem/18126
import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())

Tree=[ [] for _ in range(N+1) ]
for i in range(1, N):
    a, b, c = map(int, sys.stdin.readline().split())
    Tree[a].append([b, c])
    Tree[b].append([a, c])

distances = [0] * (N+1)

# graph: (목적지, 거리), v:시작점
def dfs(graph, v):
        for end, distance in graph[v]:
            if distances[end] is 0  and end is not 1:
                distances[end] = distances[v] + distance
                dfs(graph, end)
                
dfs(Tree,1)
print(max(distances))


# 4
# 1 4 2
# 1 2 1
# 4 3 1