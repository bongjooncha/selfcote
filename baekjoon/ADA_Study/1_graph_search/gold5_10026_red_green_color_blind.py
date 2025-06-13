# https://www.acmicpc.net/problem/10026

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
origin = []
blind = []

for _ in range(N):
    row = list(input().strip())
    origin.append(row)
    blind.append(['G' if c == 'R' else c for c in row])

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def sol(x,y,color,grid):
    if not (0 <= x < N and 0 <= y < N) or grid[x][y] != color:
        return 0
    
    grid[x][y] = '0'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        sol(nx, ny, color, grid)

    return 1

origin_count = 0
for i in range(N):
    for j in range(N):
        if origin[i][j] in 'RGB':
            origin_count += sol(i, j, origin[i][j], origin)

blind_count = 0
for i in range(N):
    for j in range(N):
        if blind[i][j] in 'GB':
            blind_count += sol(i, j, blind[i][j], blind)

print(origin_count, blind_count)