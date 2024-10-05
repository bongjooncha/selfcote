import sys
import math

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ans = 1
    for i in range(a):
        ans *= b-i
    ans //= math.factorial(a)
    print(ans)


# for _ in range(n):
#     a, b = map(int,sys.stdin.readline.split())
#     ans = math.comb(b,a)
#     print(ans)