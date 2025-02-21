# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
M = [int(input()) for _ in range(N)]
M.sort()

counter = Counter(M)
ms = counter.most_common()

max_count = ms[0][1]

print(round(sum(M)/N))
print(M[int(round(N/2,1))])
try:
    if ms[0][1] == ms[1][1]:
        print(ms[1][0])
    else:
        print(ms[0][0])
except:
        print(ms[0][0])
print(M[N-1]-M[0])