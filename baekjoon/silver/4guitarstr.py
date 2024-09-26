# https://www.acmicpc.net/problem/1049

n, m = map(int,input().split())

lp, ls = 1000, 1000

for _ in range(m):
    p, s = map(int,input().split())
    lp = min(p,lp)
    ls = min(s,ls)

pack = n // 6
sing = n % 6
ans = 0

if lp >= ls * 6:
    ans = ls * 6 * pack
else:
    ans = lp * pack

if lp >= ls * sing:
    ans += ls *sing
else:
    ans += lp

print(ans)

    
