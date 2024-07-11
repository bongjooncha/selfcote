import sys
sys.setrecursionlimit(100000)


N = int(input())
edges = []
index = 1
for i in range(N-1):
    u, v = map(int, input().split())
    edges.append((u, v))
    index += 2
    
tree = [[] for _ in range(N + 1)]
for u, v in edges:
    tree[u].append(v)
    tree[v].append(u)


scores = [0] * (N + 1)
visited = [False] * (N + 1)

def dfs(node):
    visited[node] = True
    total_score = 0
    can_win = False
    
    for child in tree[node]:
        if not visited[child]:
            child_score, child_can_win = dfs(child)
            total_score += child_score
            can_win = can_win or child_can_win
    
    current_score = total_score + node
    if total_score >= current_score or not can_win:
        can_win = True
    else:
        can_win = False
    
    scores[node] = can_win
    return current_score, can_win

dfs(1)

for i in range(1, N + 1):
    print(1 if scores[i] else 0)

