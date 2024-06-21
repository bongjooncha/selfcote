#https://softeer.ai/practice/6293
# N은 3e3, 돌은 1e8이하

N = int(input())
hights = list(map(int, input().split()))

ans = [1]*N

for i in range(1,N):
    for j in range(i):
        if hights[i] > hights[j]:
            ans[i] = max(ans[i],ans[j]+1)
print(ans[-1])