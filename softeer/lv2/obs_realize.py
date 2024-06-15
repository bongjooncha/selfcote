# https://softeer.ai/practice/6282
# 1이 장애물, 0이 도로, 정사각형으로 주어짐
# 장애물 수를 오름차순으로 출력

N = int(input())
road = [list(map(int,input())) for _ in range(N)]

def dfs(x, y):
    # 스택을 이용한 DFS 구현
    stack = [(x, y)]
    count = 0
    
    while stack:
        x, y = stack.pop()
        if 0 <= x < N and 0 <= y < N and road[x][y] == 1:
            road[x][y] = -1  # 방문 처리
            count += 1
            # 상하좌우 탐색
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))
    
    return count

block_sizes = []

for i in range(N):
    for j in range(N):
        if road[i][j] == 1:
            block_size = dfs(i, j)
            block_sizes.append(block_size)

# 결과 출력
print(len(block_sizes))
block_sizes.sort()
for size in block_sizes:
    print(size)