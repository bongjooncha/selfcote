# https://www.acmicpc.net/problem/1009

N = int(input())
results = []
for _ in range(N):
    a, b = map(int, input().split())
    if b %4 !=0:
        b = b % 4
    else:
        b = 4
    a = a % 10
    if a == 0 :
        ans = 10
    else:
        ans = a**b%10
    print(ans)