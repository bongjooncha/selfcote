# https://softeer.ai/practice/7628
# N은 100이하, 난로역시 100이하

N = int(input())
radis = list(map(int,input().split()))

ans = [0]*(max(radis)+1)
for i in range(2,max(radis)+1):
    ok = 0
    for radi in radis:
        if radi % i ==0:
            ok += 1
    ans[i] = ok

print(max(ans))