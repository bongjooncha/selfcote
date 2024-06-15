# N x M의 맵, 육지와 바다 주어짐
# A는 북쪽에서 떨어진, B는 서쪽에서 떨어진 거리
# 현재위치에서 왼쪽방향부터 차레대로 감
# 왼쪽에 아직 못가본데가 있음 전진
# 이미 다 가봤거나 모두 바다라면 멈춤

#N이 세로좌표, M이 가로좌표
N, M = map(int, input().split())
#Direction 0:북, 1: 동, 2: 남, 3: 서
A, B, D = map(int, input().split())
#0: 육지, 1: 바다
graph = [list(map(int, input().split())) for _ in range(N)]

move = [[-1,0],[0,1],[1,0],[0,-1]]

block = 1
turn = 0
graph[A][B] = 1

while turn < 4:
    if graph[A + move[D][0]][B + move[D][1]] == 0:
        graph[A + move[D][0]][B + move[D][1]] = 1
        A += move[D][0]
        B += move[D][1]
        turn = 0
        block += 1
    else:
        D = (D + 3) % 4
        turn += 1

print(block)

# input
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

