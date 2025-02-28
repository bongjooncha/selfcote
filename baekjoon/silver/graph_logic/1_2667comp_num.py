# https://www.acmicpc.net/problem/2667
# silver 1
# graph(dfs/bfs)

import sys

input = sys.stdin.readline

N = int(input())
APT = [list(map(int,input().strip())) for _ in range(N)]
vis = [[False]*N for _ in range(N)]


ans=[]

for i in range(N):
    for j in range(N):
        if APT[i][j] ==1 and not vis[i][j]:
            