# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())

times = sorted([list(map(int, input().split())) for _ in range(n)],
               key = lambda x: (x[1], x[0]))

end = 0
ans = 0

for s,e in times:
    if end <= s:
        ans += 1
        end = e
print(ans)

