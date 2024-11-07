# https://www.acmicpc.net/problem/1193

n = int(input())

i = 1 # 분모 분자 합
k = 1 # 해당 라인 마지막 수

while n > k:
    i += 1
    k += i

i += 1
a = k-n+1  #(분모)
if i %2 ==1:
    print(f'{i-a}/{a}')
else:
    print(f'{a}/{i-a}')


