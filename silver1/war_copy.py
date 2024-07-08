# https://www.acmicpc.net/problem/1303

# W가 우리팀, B가 상대
import sys
sys.setrecursionlimit(10**9)

N, M = map(int,input().split())
warriers = [list(input()) for _ in range(M)]


def dfs(who,x,y,point):
    if 0<=x<N and 0<=y<M and warriers[y][x] == who:
        warriers[y][x] = 0
        point += 1

        point = dfs(who,x+1,y,point)
        point = dfs(who,x-1,y,point)
        point = dfs(who,x,y+1,point)
        point = dfs(who,x,y-1,point)
    return point

me_sum=0
oppo_sum=0

for i in range(N):
    for j in range(M):
        if warriers[j][i] != 0:
            me = dfs('W',i,j,0)
            me_sum += me **2
        if warriers[j][i] != 0:
            oppo = dfs('B',i,j,0)
            oppo_sum += oppo **2
print(me_sum,oppo_sum)