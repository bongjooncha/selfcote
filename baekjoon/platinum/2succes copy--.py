from collections import deque

def bfs(N, M, D, grid):
    queue = deque([(0, 0, 0)])  # (row, col, explosions)
    visited = set([(0, 0)])
    
    while queue:
        r, c, explosions = queue.popleft()
        
        if r == N-1 and c == M-1:
            return explosions
        
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited:
                if grid[nr][nc] == '.':
                    queue.appendleft((nr, nc, explosions))
                    visited.add((nr, nc))
                else:
                    exploded = False
                    for i in range(max(0, nr-D+1), min(N, nr+D)):
                        for j in range(max(0, nc-D+1), min(M, nc+D)):
                            if grid[i][j] == '#':
                                exploded = True
                                grid[i][j] = '.'
                    if exploded:
                        queue.append((nr, nc, explosions + 1))
                        visited.add((nr, nc))
    
    return -1  # 도달할 수 없는 경우

N, M, D = map(int, input().split())
grid = [list(input().strip()) for _ in range(N)]

result = bfs(N, M, D, grid)
print(result)