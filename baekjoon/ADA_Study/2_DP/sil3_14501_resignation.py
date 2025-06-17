# https://www.acmicpc.net/problem/14501

'''
N+1일째 날에 퇴사. N일 동안 상담진행.
Ti는 걸리는 기간 Pi는 금액.

n일+Ti일 날 상담 가능. 이때까지 최대 값을 확인해야함.
'''

N = int(input())
LISTS = [[]]
for i in range(N):
    LISTS.append(list(map(int,input().split())))

def sol(n,lists):
    dp = [0] * (n + 1)
    
    for i in range(1,n+1):
        if i + lists[i][0] <= n: 
            dp[i + lists[i][0]] = max(dp[i + lists[i][0]], dp[i] + lists[i][1])
        dp[i + 1] = max(dp[i + 1], dp[i]) 
    
    print(dp[n])


sol(N,LISTS)