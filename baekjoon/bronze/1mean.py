# https://www.acmicpc.net/problem/1546

n = int(input())
arr = list(map(int,input().split()))
big = max(arr)

ans = 0
for i in arr:

     ans += i/big * 100

print(ans/n)