# https://www.acmicpc.net/problem/2178
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

maps = [list(map(int,input().strip())) for _ in range(n)]

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    que = deque([(x,y)])

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny <0 or ny >= m:
                continue
            if maps[nx][ny] ==0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                que.append((nx,ny))

    return maps[n-1][m-1]

print(bfs(0,0))