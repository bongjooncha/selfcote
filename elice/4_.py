from collections import deque, defaultdict

N = int(input())


tree = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = [-1]*(N+1)
ans[1] = 0


for i in range(N+1):
    for j in tree[i]:
        if len(tree[i]) == 1:
            ans[i]=0
        elif ans[j] == -1:
            ans[j]=ans[i]+1

print(ans)
for i in range(1,N+1):
    a = ans[i]
    if a%2 ==0:
        print(1)
    else:
        print(0)