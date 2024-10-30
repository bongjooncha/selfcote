# https://www.acmicpc.net/problem/1021

N, M = map(int,input().split())
num_list = list(map(int,input().split()))
num = list(range(1,N+1))
ans = 0

for i in num_list:
    l = len(num)
    a = num.index(i)
    if a+1 <= (l+1)/2:
        ans += a
    else:
        ans += l-a
    num = num[a+1:] + num[:a] 

print(ans)


        