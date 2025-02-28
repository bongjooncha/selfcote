# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

import sys

# 입력 처리
input = sys.stdin.readline
n = int(input())
map_data = []
for _ in range(n):
    map_data.append(list(map(int, input().strip())))

# 방문 여부를 저장할 배열
visited = [[False] * n for _ in range(n)]

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]  # 상하좌우 행 이동
dy = [0, 0, -1, 1]  # 상하좌우 열 이동

# DFS 함수 정의
def dfs(x, y):
    # 현재 위치가 지도 범위를 벗어나거나, 집이 없는 곳이거나, 이미 방문한 곳이면 0 반환
    if x < 0 or x >= n or y < 0 or y >= n or map_data[x][y] == 0 or visited[x][y]:
        return 0
    
    # 현재 위치 방문 처리
    visited[x][y] = True
    
    # 현재 집을 포함하여 1로 초기화
    count = 1
    
    # 상하좌우 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        count += dfs(nx, ny)
    
    return count

# 단지 정보를 저장할 리스트
complexes = []

# 모든 위치에 대해 DFS 수행
for i in range(n):
    for j in range(n):
        if map_data[i][j] == 1 and not visited[i][j]:
            # 새로운 단지 발견
            house_count = dfs(i, j)
            complexes.append(house_count)

# 단지 내 집의 수를 오름차순으로 정렬
complexes.sort()

# 결과 출력
print(len(complexes))  # 총 단지 수
for count in complexes:
    print(count)  # 각 단지 내 집의 수 