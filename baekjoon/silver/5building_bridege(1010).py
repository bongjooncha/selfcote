# https://www.acmicpc.net/problem/1010
from math import factorial

N = int(input())
for i in range(N):
    a,b = map(int,input().split())
    ans = factorial(b)//(factorial(a)*factorial(b-a))
    print(ans)
