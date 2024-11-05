# https://www.acmicpc.net/problem/2606
import sys 

input = sys.stdin.readline

n = int(input())
lan = int(input())
lans = [list(map(int,input().split())) for _ in range(lan)]

comps = [False for _ in range(n+1)]
comps[1] = True

def dfs(start):
    global comps
    for l in lans:
        if start == l[0]:
            if comps[l[1]] == False:
                comps[l[1]] = True
                dfs(l[1])
        elif start == l[1]:
            if comps[l[0]] == False:
                comps[l[0]] = True
                dfs(l[0])
                
dfs(1)

print(comps.count(True)-1)

