# https://www.acmicpc.net/problem/1004

T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int,input().split())
    N = int(input())
    ans = 0
    for i in range(N):
        x,y,r = map(int,input().split())
        st =(x1-x)**2+(y1-y)**2
        en = (x2-x)**2+(y2-y)**2
        rsq = r**2
        if st 
        if st > rsq and en > rsq:
            pass
        else:
            ans +=1
    print(ans)