# https://www.acmicpc.net/problem/2468
# silver1
# graph(dfs)

import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
maps = [list(map(int,input().strip().split())) for _ in range(N)]
max_height = max(max(row) for row in maps)
dx, dy = [-1,1,0,0],[0,0,-1,1]


def dfs(x,y,height):
    if x<0 or x>=N or y<0 or y>=N or visited[x][y] or maps[x][y] <= height:
        return
    visited[x][y] = True
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        dfs(nx,ny,height)

safe_height = 0
ans = 0

for height in range(max_height):
    visited = [[False]*N for _ in range(N)]
    safe_area = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and maps[i][j] >height:
                dfs(i,j,height)
                safe_area += 1
    ans = max(ans,safe_area)

print(ans)



