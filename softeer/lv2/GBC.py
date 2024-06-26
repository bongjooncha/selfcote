#https://softeer.ai/practice/6270

N, M = map(int, input().split())

# 운행길이, 운행속도
N_SPEEDS = [list(map(int, input().split())) for _ in range(N)]
M_SPEEDS = [list(map(int, input().split())) for _ in range(M)]

for i in range(1,len(N_SPEEDS)):
    N_SPEEDS[i][0] += N_SPEEDS[i-1][0]
    
for i in range(1,len(M_SPEEDS)):
    M_SPEEDS[i][0] += M_SPEEDS[i-1][0]

ans = 0
j = 0
for i in range(len(M_SPEEDS)):
    md = M_SPEEDS[i][0]
    ms = M_SPEEDS[i][1]
    while md > N_SPEEDS[j][0]:
        j += 1
    ns = N_SPEEDS[j][1]
    if ms - ns >= 0:
        ans = max(ans,ms - ns)
for i in range(len(N_SPEEDS)):
    nd = N_SPEEDS[i][0]
    ns = N_SPEEDS[i][1]
    while nd > M_SPEEDS[j][0]:
        j += 1
    ms = M_SPEEDS[j][1]
    if ms - ns >= 0:
        ans = max(ans,ms - ns)

print(ans)


# _2에서 해결. 전체를 확인 안하고 check마지막 지점에서만 확인해서 틀림