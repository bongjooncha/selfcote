# https://www.acmicpc.net/problem/2178
# silver1
# graph(bfs)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
MAP = [list(map(int, input().strip())) for _ in range(N)]

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = deque([(x,y)])
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or MAP[nx][ny] == 0:
                continue
            if MAP[nx][ny] == 1:
                MAP[nx][ny] = MAP[x][y] + 1
                que.append((nx,ny))
    return MAP[N-1][M-1]

print(bfs(0,0))


