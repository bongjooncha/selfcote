# https://www.acmicpc.net/problem/1284

numbs = []
a = '1'
while a != '0':
    a = input()
    numbs.append(a)

for i in range(len(numbs)-1):
    ans = 1
    for numb in numbs[i]:
        if numb == '1':
            ans += 3
        elif numb == '0':
            ans += 5
        else:
            ans += 4
    print(ans)