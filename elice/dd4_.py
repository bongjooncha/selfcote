from collections import defaultdict

N = int(input())


tree = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

road = [[0, -1] for _ in range(N+1)]
road[1] = [1,0]

for index,i in enumerate(range(1,N+1)):
    for j in tree[i]:
        if road[j][1] == -1:
            road[j] = [index,road[i][1]+1]
print(road)