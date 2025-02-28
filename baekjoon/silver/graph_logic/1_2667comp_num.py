# https://www.acmicpc.net/problem/2667
# silver 1
# graph(dfs/bfs)

import sys

input = sys.stdin.readline

N = int(input())
APT = [list(map(int,input().strip())) for _ in range(N)]
vis = [[False]*N for _ in range(N)]


ans=[]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x < 0 or y < 0 or x >= N or y >= N or APT[x][y]==0 or vis[x][y]:
        return 0
    vis[x][y] = True
    count = 1 
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        count += dfs(nx,ny)
    return count

for i in range(N):
    for j in range(N):
        if APT[i][j] ==1 and not vis[i][j]:
            ans.append(dfs(i,j))

ans.sort()
print(len(ans))
print(*ans, sep = '\n')
