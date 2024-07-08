from collections import deque

def minimum_walls_to_break(N, M, grid):
    # 방향벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 초기 상태 설정
    deque_bfs = deque()
    deque_bfs.append((0, 0))
    
    # 방문과 벽 부순 횟수를 저장하는 배열
    dist = [[float('inf')] * M for _ in range(N)]
    dist[0][0] = 0
    
    while deque_bfs:
        r, c = deque_bfs.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < M:
                new_dist = dist[r][c] + grid[nr][nc]
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    if grid[nr][nc] == 1:
                        deque_bfs.append((nr, nc))
                    else:
                        deque_bfs.appendleft((nr, nc))
    
    return dist[N-1][M-1]

# 입력 받기
M, N = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

# 최소 벽 부수기 횟수 출력
print(minimum_walls_to_break(N, M, grid))
