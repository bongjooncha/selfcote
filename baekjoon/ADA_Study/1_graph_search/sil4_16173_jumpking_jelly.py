# https://www.acmicpc.net/problem/16173
# N은 2혹은 3 /// 마지막 칸은 -1, 나머지는 0~100

##풀이

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
MAPS = [list(map(int,input().split())) for _ in range(N)]

# # BFS (56ms)
# def bfs(n,maps):
#     queue = deque([(0,0)])
#     visited = [[False]*n for _ in range(n)]
#     visited[0][0] = True

#     while queue:
#         x,y = queue.popleft()
#         jump = maps[x][y]
#         if jump == -1:
#             return True
        
#         for dx,dy in [(0,jump),(jump,0)]:
#             nx,ny = x+dx,y+dy
#             if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#     return False

# print("HaruHaru" if bfs(N,MAPS) else "Hing")
        

# DFS (36ms)
def dfs(n, maps):
    class DFS_solve:
        def __init__(self, n, maps):
            self.n = n
            self.maps = maps
            self.visited = [[False] * n for _ in range(n)]
            self.visited[0][0] = True

        def solve(self, x, y):
            jump = self.maps[x][y]
            if jump == -1:
                return True
            
            for dx, dy in [(0, jump), (jump, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.n and 0 <= ny < self.n and not self.visited[nx][ny]:
                    self.visited[nx][ny] = True
                    if self.solve(nx, ny):
                        return True
            return False
    
    solver = DFS_solve(n, maps)
    return solver.solve(0, 0)

print("HaruHaru" if dfs(N, MAPS) else "Hing")


''' grid
N이 2인 경우:
(0,0)이 무조건 1이어야함 and 이후 (0,1),(1,0) 둘중 하나가 1 => 아니라면 실패

N이 3인 경우:
중간 위치 설정. 중간 위치까지 가는 경우를 넣고, 중간 위치에서 도착지까지 가는 방법 탐색
'''

# # super grid (36ms)
# def super_grid(n,maps):
#     def grid_2(maps):
#         if maps[0][0] == 1 and (maps[0][1] == 1 or maps[1][0] == 1):
#             return True
#         else: return False

#     def grid_3(maps):
#         # maps[1][1]에서 도달하는 경우
#         if grid_2(maps) and maps[1][1] == 1:
#             if maps[1][2] == 1 or maps[2][1] == 1:
#                 return True
#         # maps[0][2] or maps[2][0]에 도달하는 경우
#         if grid_2(maps) or maps[0][0] == 2:
#             if maps[0][2] == 2 or maps[2][0] == 2:
#                 return True
#             if (maps[0][2] ==1 and maps[1][2] ==1) or (maps[2][0]==1 and maps[2][1]==1):
#                 return True
#         # maps[1][2], maps[2][1] 이 2인경우
#         if maps[0][0] == 1:
#             if (maps[0][1] == 2 and maps[2][1] ==1) or (maps[1][0] == 2 and maps[1][2] ==1):
#                 return True
#         else: return False

#     if n == 2:
#         return grid_2(maps)
#     elif n == 3:
#         return grid_3(maps)

print("HaruHaru" if super_grid(N,MAPS) else "Hing")

