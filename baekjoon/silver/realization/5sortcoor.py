# https://www.acmicpc.net/problem/11650

import sys

input = sys.stdin.readline

n = int(input())

cords = [list(map(int,input().strip().split())) for _ in range(n)]

cords.sort(key= lambda x: x[1])
cords.sort()
for cord in cords:
    print(cord[0], cord[1])