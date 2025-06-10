# https://www.acmicpc.net/problem/17086
#

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(N)]

cases = [-1,0,1]
moves = [(dx,dy) for dx in cases for dy in cases if not (dx == 0 and dy == 0)]


def solv(n,m,grid):
    queue = deque()
    visited = [[-1] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i,j))
                visited[i][j] = 0

    distance = 0
    while queue:
        x,y = queue.popleft()

        for dx, dy in moves:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))
                distance = max(distance, visited[nx][ny])

    return distance

print(solv(N,M,maps))

