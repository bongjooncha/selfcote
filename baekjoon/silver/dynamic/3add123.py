# https://www.acmicpc.net/problem/9095

T = int(input())
ans = [1,2,4,7,13,24,44,81,149,274]
for i in range(T):
    n = int(input())
    print(ans[n-1])

