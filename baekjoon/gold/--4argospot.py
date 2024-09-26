# https://www.acmicpc.net/problem/1261

from collections import deque

N, M = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(M)]
maze_break = [[1e4]*N for _ in range(M)]

def bfs():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    queue = deque()
    queue.append((0,0,0))

    while queue:
        x, y, n = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                new_break = n + maze[ny][nx]
                if new_break < maze_break[ny][nx]:
                    maze_break[ny][nx] = new_break
                    if maze[ny][nx] == 1:
                        queue.append((ny,nx,n+1))
                    else: queue.appendleft((ny,nx,n))
        return maze_break[M-1][N-1]
print(bfs())



                