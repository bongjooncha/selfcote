from collections import defaultdict

N = int(input())


tree = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 위치, 번호
road = [[-1, 0] for _ in range(N+1)]
road[1] = [0,1]

for i in range(N+1):
    for j in tree[i]:
        if road[j][0] == -1:
            road[j] = [road[i][0]+1,j]
k = sorted(road, reverse=True)
ans = [-1]*(N+1)

#i => 위치[0], 번호[1]
for i in k:
    if len(tree[i[1]])==1:
        ans[i[1]]=i[1]
    elif i[1]==0:
        pass
    else:
        # if로 i의 위치보다 뒤에 있는 j 찾음
        befor = min([ans[j] for j in tree[i[1]] if road[j][0] > i[0]])
        ans[i[1]] = i[1] - befor 

for i in range(1,N+1):
    if ans[i] > 0:
        print(1)
    else:
        print(0)
