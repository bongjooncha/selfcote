# https://www.acmicpc.net/problem/2667
import sys

input = sys.stdin.readline

N = int(input())
MAPS = [list(map(int,input().strip())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def solv(x,y):
    if not (0 <= x <N and 0 <= y < N) or MAPS[x][y] != 1:
        return 0
    
    MAPS[x][y]= 0
    count = 1

    for i in range(4):
        count += solv(x+dx[i],y+dy[i])
    
    return count

ans = []
for i in range(N):
    for j in range(N):
        if MAPS[i][j] == 1:
            ans.append(solv(i,j))


print(len(ans))
for size in sorted(ans): 
    print(size)