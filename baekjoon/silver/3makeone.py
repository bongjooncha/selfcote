# https://www.acmicpc.net/problem/1463

# n은 10^6이하
n = int(input())

ans = [0,0,1,1]
for i in range(4,n+1):
    a, b, c = float('inf'),float('inf'),float('inf')
    if i % 3 ==0:
        a = ans[i//3]+1
    if i%2 ==0:
        b = ans[i//2]+1
    c = ans[i-1]+1
    ans.append(min(a,b,c))
print(ans[n])



