# https://www.acmicpc.net/problem/2178
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graphs = [list(map(int,input().strip())) for _ in range(n)]

def bfs(a,b):
    que = deque()
    que.append((a,b))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx< n and 0 <= ny < m and graphs[nx][ny] ==1:
                graphs[nx][ny] = graphs[x][y]+1
                que.append((nx,ny))
                   
    return graphs[n-1][m-1]

print(bfs(0,0))