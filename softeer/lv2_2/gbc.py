N, M = map(int, input().split())
limits = [list(map(int,input().split())) for _ in range(N)]
true_speeds = [list(map(int,input().split())) for _ in range(M)]

for i in range(1,len(limits)):
    limits[i][0] += limits[i-1][0]
check = [a[0] for a in limits]
for i in range(1,len(true_speeds)):
    true_speeds[i][0] += true_speeds[i-1][0]
    
for true in true_speeds:
    if true[0] not in check:
        check.append(true[0])
check.sort()

l=0
t=0
ans = 0
for d in check:
    while d > limits[l][0] and limits[l][0] < 100:
        l +=1
    while d > true_speeds[t][0] and true_speeds[t][0] < 100:
        t +=1
    ans = max(ans, true_speeds[t][1]-limits[l][1])
print(ans)
    