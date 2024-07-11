from collections import deque, defaultdict

N = int(input())


tree = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = [-1]*(N+1)

for i in range(N,0,-1):
    if i > max(tree[i]):
        ans[i]=i
    else:
        befor = 1e9
        befor = min([ans[j] for j in tree[i] if j > i])
        ans[i] = i-befor

for i in range(1,N+1):
    if ans[i] > 0:
        print(1)
    else:
        print(0)
