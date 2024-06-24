# https://softeer.ai/practice/6282

N = int(input())

GRAPH = [list(map(int, input())) for _ in range(N)]
print(GRAPH)

def bfs(x,y, ans):
    if 0 <= x < N and 0 <= y < N and GRAPH[x][y] == 1:
        GRAPH[x][y] = 0
        ans += 1
        ans = bfs(x-1,y, ans)
        ans = bfs(x,y-1, ans)
        ans = bfs(x+1,y, ans)
        ans = bfs(x,y+1, ans)
        return ans
    else: return ans

answers = []

for i in range(N):
    for j in range(N):
        ans = 0
        ans = bfs(i,j,ans)
        if ans != 0:
            answers.append(ans)
            
answers.sort()
print(len(answers))
for answer in answers:
    print(answer)