# https://www.acmicpc.net/problem/1463

n = int(input())

ans = [0,0,1,1]

if n <= 3:
    print(ans[n])
else:
    for i in range(4,n+1):
        a = 10**6
        if i % 3 == 0:
            a = min(a,ans[i//3]+1)
        if i %2 ==0:
            a = min(a,ans[i//2]+1)
        a = min(a,ans[i-1]+1)
        ans.append(a)
    print(ans[n])