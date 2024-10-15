# https://www.acmicpc.net/problem/11047

import sys

input = sys.stdin.readline
N, K = map(int, input().split())

coins = []

for _ in range(N):
    a = int(input())
    if a <= K:
        coins.append(a)
    else:
        pass

ans = 0
for i in reversed(coins):
    ans += K // i
    K %= i
print(ans)

