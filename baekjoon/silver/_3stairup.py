# https://www.acmicpc.net/problem/2579

import sys

n = int(sys.stdin.readline())

stairs = [0]

for _ in range(n):
    stairs.append(int(sys.stdin.readline()))

if n>=2:
    ans = [0,stairs[1],stairs[1]+stairs[2]]

    for i in range(3,n+1):
        ans.append(max(stairs[i]+ans[i-2],stairs[i]+stairs[i-1]+ans[i-3]))
else:
    ans =[0,stairs[1]]

print(ans[n])


# 3번 연속 계단 사용 불가, 1개 계단 스킵 가능
# 최대 점수 필요, 마지막 계단 필수적


