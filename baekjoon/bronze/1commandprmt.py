# https://www.acmicpc.net/problem/1032

n = int(input())

ans = []
for _ in range(n):
    s = list(input())
    if ans == []:
        ans = s
    else:
        for i in range(len(ans)):
            if ans[i] != s[i]:
                ans[i] = "?"

print(''.join(ans))
    