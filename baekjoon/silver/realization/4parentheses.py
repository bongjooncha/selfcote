# https://www.acmicpc.net/problem/9012

n = int(input())

for i in range(n):
    l = list(map(str,input()))
    ans = 0
    for j in l:
        if ans == -1:
            break
        elif j == '(':
            ans +=1
        else:
            ans -=1
    if ans == 0:
        print('YES')
    else:
        print('NO')