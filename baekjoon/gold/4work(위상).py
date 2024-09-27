# https://www.acmicpc.net/problem/2056
from collections import deque

N = int(input())

graph = [[],[]]
time = [0]

for i in range(N):
    info = list(map(int,input().split()))
    time.append(info[0])
    if info[1] != 0:
        graph.append(info[2:])

for i in range(1,N+1):


print(max(time))