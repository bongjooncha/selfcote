# N x M 형태의 카드
# 뽑고자하는 카드가 포함된 행을 선택, 이후 가장 작은 수를 뽑아야함


N, M = map(int, input().split())
cards = [list(map(int,input().split())) for i in range(N)]

ans = []
for card in cards:
    ans.append(min(card))

print(max(ans))

# input 
# 3 3
# 3 1 2
# 4 1 3
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4