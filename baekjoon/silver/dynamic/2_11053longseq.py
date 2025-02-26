# https://www.acmicpc.net/problem/11053

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

#모든 경우를 다 해보는 방법. 만일 이전에 비교완료했던 부분을 지울 경우 더 빨리 처리할수 있을 것으로 보임