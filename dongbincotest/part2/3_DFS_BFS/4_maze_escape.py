# N x M 크기 직사각형
# 0에 괴물, 1에 괴물 없음
# 탈출을 위한 최소 칸의 개수

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]

print(bfs(0,0))



# input
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111