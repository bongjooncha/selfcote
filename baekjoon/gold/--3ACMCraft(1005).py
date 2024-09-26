# https://www.acmicpc.net/problem/1005

# T: 테스트 회수
T = int(input())

# N: 건물개수, K: 규칙 개수, N_Time: 건물 시간, N_order: 규칙(선, 후), W: 마지막 건물
for i in range(T):
    N, K = map(int,input().split())
    N_Time = list(map(int,input().split()))
    N_Order = [list(map(int,input().split())) for _ in range(K)]
    W = int(input())
    
    Time_map = [[] for _ in range(N+1)]

    for order in N_Order:
        s,e = order
        Time_map[s].append(e)

    ans_list = []





    