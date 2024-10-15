# https://www.acmicpc.net/problem/1929
# 곱하여 값이 나오기 위해서는 자기 자신에게 루트를 한 수의 제곱 혹은 (자기보다 큰수)* (자기보다 작은수)를 통해 나온다.
# 따라서 루트한 자신 이하의 수만 확인하면 된다.

m, n = map(int,input().split())

for i in range(m,n+1):
    if i == 1:
        continue
    
    for j in range(2, int(i**0.5) + 1): 
        if i % j == 0: 
            break
    else:
        print(i)


