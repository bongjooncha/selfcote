# https://www.acmicpc.net/problem/1932
import sys

input = sys.stdin.readline

tri = []
n = int(input())
for _ in range(n):
    tri.append(list(map(int,input().split())))

ans_tri=[[] for _ in range(n)]
ans_tri[0] = tri[0]

for i in range(1,n):
    for index,j in enumerate(tri[i]):
        a,b = 0,0
        if index > 0:
            a=j+ans_tri[i-1][index-1]
        try:
            b = max(a,j+ans_tri[i-1][index])
        except IndexError:
            pass
        ans_tri[i].append(max(a,b))
print(max(ans_tri[n-1]))

