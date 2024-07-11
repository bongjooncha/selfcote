import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    if not tree[node]:  # 리프 노드인 경우
        dp[node] = 1
        return
    
    for child in tree[node]:
        dfs(child)
        
    if any(dp[child] == 0 for child in tree[node]):
        dp[node] = 1  # 자식 중 하나라도 지는 경우가 있으면 이김
    else:
        dp[node] = 0  # 모든 자식이 이기는 경우면 짐

# 입력 받기
n = int(input())
tree = [[] for _ in range(n+1)]
dp = [0] * (n+1)

for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 루트 노드를 1로 가정하고 트리 구조화
def make_tree(node, parent):
    for i in range(len(tree[node])):
        if tree[node][i] == parent:
            tree[node].pop(i)
            break
    for child in tree[node]:
        make_tree(child, node)

make_tree(1, 0)

# DFS로 각 노드의 승패 여부 계산
dfs(1)

# 결과 출력
for i in range(1, n+1):
    print(dp[i])