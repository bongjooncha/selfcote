# https://www.acmicpc.net/problem/2941
alphas = input()

ans = len(alphas)

for i in range(len(alphas)):
    try:
        if alphas[i] == 'c':
            if alphas[i+1] == '=' or alphas[i+1] == '-':
                ans -= 1
        elif alphas[i] == 'd':
            if (alphas[i+1] == 'z' and alphas[i+2] =='=') or alphas[i+1] == '-':
                ans -= 1
        elif alphas[i] == 'l' or alphas[i] == 'n':
            if alphas[i+1] == 'j':
                ans -=1
        elif alphas[i] == 's' or alphas[i] == 'z':
            if alphas[i+1] == '=':
                ans -= 1
    except IndexError:
        continue
print(ans)
    