# https://www.acmicpc.net/problem/1003
import sys

input = sys.stdin.readline

n = int(input())

fibo = [[0,0] for _ in range(41)]
fibo[0] = [1,0]
fibo[1] = [0,1]
num = []

for _ in range(n):
    a = num.append(int(input()))

for i in range(2,max(num)+1):
    fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]


for i in num:
    print(*fibo[i])