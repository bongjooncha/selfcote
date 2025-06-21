# https://www.acmicpc.net/problem/14501

'''
N+1일째 날에 퇴사. N일 동안 상담진행.
Ti는 걸리는 기간 Pi는 금액.

(n + Ti)일에 해당하는 날짜의 최대값을 순차적으로 구하기.
1일 부터 n일 까지 점차 올라가면서 최대 값 구하기
'''

N = int(input())
LISTS = [[]]
for i in range(N):
    LISTS.append(list(map(int,input().split())))

def sol(n,lists):
    dp = [0] * (n + 2)
    
    for i in range(1,n+1):
        day = i + lists[i][0]
        dp[i] = max(dp[:i+1])
        if day <= n+1: 
            dp[day] = max(dp[day],dp[i]+lists[i][1])
            
    return max(dp)


print(sol(N,LISTS))