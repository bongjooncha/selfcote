# https://www.acmicpc.net/problem/1002

# 조, 백 x,y 좌표 2개 주어짐. 상대편 류 거리 주어짐
# 있을 수 있는 위치 개수 출력

N = int(input())

for i in range(N):
    info = list(map(int, input().split()))
    if (info[0]==info[3] and info[1]==info[4]):
        if info[2]==info[5]:
            print(-1)
        else:
            print(0)
        
    else:
        distance = ((info[0]-info[3])**2 + (info[1]-info[4])**2)**(1/2)
        radi = info[2]+info[5]
        if distance + info[2] < info[5] or distance+info[5]<info[2]:
            print(0)
        elif distance + info[2] == info[5] or distance+info[5] == info[2]:
            print(1)
        elif distance > radi:
            print(0)
        elif distance == radi:
            print(1)
        else:
            print(2)
    