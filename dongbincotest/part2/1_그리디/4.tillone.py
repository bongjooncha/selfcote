# N이 1이 될떄까지 K로 나구거나 1을 뺌.
# 근데로 나눌때는 나머지가 없어야함
# 최소 횟수 출력

N, K = map(int,input().split())

ans = 0

while N != 1:
    if N % K ==0:
        ans += 1
        N /= K
    elif N > K:
        ans += N % K
        N -= N % K
    else:
        ans += N-1
        break

print(int(ans))
