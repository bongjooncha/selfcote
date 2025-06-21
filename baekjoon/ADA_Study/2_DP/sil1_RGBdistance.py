# https://www.acmicpc.net/problem/1149
'''
연속된 집의 색은 달라야함.
모든 집을 칠할때 최솟값을 구하기.

3개의 색이 존재. 따라서 각 색이 마지막에 오는 경우 최소인 경우를 확인
'''


N = int(input())
COSTS = [list(map(int, input().split())) for _ in range(N)]

def sol(costs):
    ans=[0,0,0]
    re = [0,0,0]
    for i in costs: 
        ans[0] = i[0] + min(re[1],re[2])
        ans[1] = i[1] + min(re[0],re[2])
        ans[2] = i[2] + min(re[0],re[1])
        re = ans[:]
    return min(ans)
            
print(sol(COSTS))