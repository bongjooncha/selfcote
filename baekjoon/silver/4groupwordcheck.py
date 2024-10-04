# https://www.acmicpc.net/problem/1316
import sys
n = int(sys.stdin.readline())

ans = 0 
for _ in range(n):
    element = []
    word = sys.stdin.readline()
    for i in word:
        if i not in element:
            element.append(i)
        elif i == element[-1]:
            pass
        else:
            ans -= 1
            break
    ans+=1
    print(ans)