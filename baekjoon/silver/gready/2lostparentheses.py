# https://www.acmicpc.net/problem/1541

string = input()

ans = 0
num = ''
st = True
for s in string:
    if s == '+':
        if st == True:
            ans += int(num)
            num = ''
        else:
            ans -= int(num)
            num = ''

    elif s == '-':
        if st == True:
            ans += int(num)
            num = ''
        else:
            ans -= int(num)
            num = ''
        st = False
    else:
        num += s

if st == True:
    ans += int(num)
else:
    ans -= int(num)

print(ans)
