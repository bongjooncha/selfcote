# https://softeer.ai/practice/7374
ground = [list(map(int, input().split())) for i in range(3)]

def cost_check(list):
    if list == [1,1,1] or list == [2,2,2] or list == [3,3,3]:
        return 0
    elif list == [1,1,2] or list == [1,2,2] or list == [2,2,3] or list ==[2,3,3]:
        return 1
    else: return 2

cost = 10
while cost != 0:
    for row in ground:
        cost = min(cost_check(sorted(row)),cost)
    for col_idx in range(len(ground[0])):
        col = [row[col_idx] for row in ground]
        cost = min(cost,cost_check(sorted(col)))
    break
print(cost)
    

