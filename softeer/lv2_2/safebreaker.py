# https://softeer.ai/practice/6288

W, N = map(int,input().split())

#첫번째가 무게, 두번째가 무게 당 가격
expences = [map(int,input().split()) for _ in range(N)]

expences.sort(key=lambda x:x[1],reverse=True)
ans = 0

for expence in expences:
    if W > expence[0]:
        W -= expence[0]
        ans += expence[1] * expence[0]
    elif W == expence[0]:
        ans += expence[1] * expence[0]
        break
    else: 
        ans += expence[1] * W
        break

print(ans)
