# https://www.acmicpc.net/problem/2839

n = int(input())
ans = [0,-1,-1,1,-1,1]

if n <= 5:
    print(ans[n])
else:
    for i in range(6,n+1):
        three = ans[i-3]
        five = ans[i-5]
        if three != -1 and five != -1:
            ans.append(min(three,five)+1)
        elif three == -1 and five == -1:
            ans.append(-1)
        else:
            ans.append(max(three,five)+1)
    print(ans[n])
            


