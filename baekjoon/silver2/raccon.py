import sys
sys.setrecursionlimit(10**9)

N=int(input())
graphs = [list(map(int, input().split())) for _ in range(N-1)]
Tree=[ [] for _ in range(N+1) ]
[Tree[a].append((b, c)) for a, b, c in graphs]
[Tree[b].append((a, c)) for a, b, c in graphs]

#Node: 시작점, count: 
def DFS(Node,count):
    # 최대 길이
    global total
    # 방문 처리
    visit[Node]=True
    # i: 도착지, j 거리
    for i,j in Tree[Node]:
        if not visit[i]:
            total=max(total, count+j)
            DFS(i,count+j)

visit=[False]*(N+1)
total=0
DFS(1,0)
print(total)