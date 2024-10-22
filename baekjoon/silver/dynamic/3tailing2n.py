# https://www.acmicpc.net/problem/11726

n = int(input())

ans = [0,1,2]

if n > 2:
    for i in range(3,n+1):
        ans.append(ans[i-2]+ans[i-1])
print(ans[n]%10007)