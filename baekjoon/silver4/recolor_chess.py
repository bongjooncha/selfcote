# https://www.acmicpc.net/problem/1018

N, M = map(int,input().split())
graph = [list(input()) for _ in range(N)]

W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]


answer = 100
for i in range(N-7):
    for j in range(M-7):
        ans=0
        for index, line in enumerate(graph[i:i+8]):
            ans += sum(1 for x,y in zip(W[index],line[j:j+8]) if x!=y)
        if ans > 32:
            ans = 64 -ans
        answer = min(ans,answer)
print(answer)
            