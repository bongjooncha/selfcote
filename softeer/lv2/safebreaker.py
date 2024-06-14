# https://softeer.ai/practice/6288
# 첫줄에 W 배낭의 무게, 귀금속의 종류 N 주어짐
# 이후 금속의 무계 M과 가격 P가 주어짐
# 가장 비싸게 훔칠 수 있는 경우

W, N = map(int, input().split())
stuffs = [list(map(int,input().split())) for _ in range(N)]

stuffs.sort(key = lambda x:x[1], reverse=True)

ans = 0
i = 0
while W > 0:
    if stuffs[i][0] <= W:
        W -= stuffs[i][0]
        ans += stuffs[i][0] * stuffs[i][1]
    else:
        ans += W * stuffs[i][1]
        break
    i = i+1

print(ans)