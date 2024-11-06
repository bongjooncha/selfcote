# https://www.acmicpc.net/problem/10773

import sys

input = sys.stdin.readline

n = int(input())
nlist = []
for i in range(n):
    num = int(input())
    if num != 0:
        nlist.append(num)
    else:
        nlist.pop()
print(sum(nlist))