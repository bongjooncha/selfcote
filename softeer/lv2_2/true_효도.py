# https://softeer.ai/practice/7374
grounds = [list(map(int, input().split())) for _ in range(3)]

def cost(x):
    if x == [1,1,1] or x == [2,2,2] or x == [3,3,3]:
        return 0
    elif x == [1,1,2] or x == [1,2,2] or x== [2,2,3] or x == [2,3,3]:
        return 1
    else: return 2

ans = 3
for row in grounds:
    ans = min(ans,cost(sorted(row)))
    
for i in range(len(grounds[0])):
    col = [row[i] for row in grounds]
    ans = min(ans,cost(sorted(col)))
print(ans)