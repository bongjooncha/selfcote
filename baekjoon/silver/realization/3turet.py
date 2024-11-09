# https://www.acmicpc.net/problem/1002

import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().strip().split())
    distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    if distance == 0:
        if r1 == r2:
            print(-1)
        else: print(0)
    else:
        if distance > (r1+r2) or distance+r1 <r2 or distance+r2 <r1:
            print(0)
        elif distance == (r1+r2) or distance+r1 == r2 or distance+r2 == r1:
            print(1)
        else: print(2)