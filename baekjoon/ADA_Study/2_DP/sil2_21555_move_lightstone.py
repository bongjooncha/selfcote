# https://www.acmicpc.net/problem/21555

'''
돌을 끌고 올라가면 비용 Ai, 들고 올라가면 Bi, 방식을 바꿀때 마다 K 비용이 듬. 

들고가는 경우 가장 싼 경우와 끌고가는 경우 가장 싼경우 비교.
'''

N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
max_value = float('inf')

def sol(n,k,a,b):
    hold = [[max_value]] * n
    carry = [[max_value]] * n

    hold[0] = a[0]
    carry[0] = b[0]

    for i in range(1, n):
        hold[i] = min(hold[i-1],carry[i-1]+k)+a[i]
        carry[i] = min(carry[i-1],hold[i-1]+k)+b[i]
    
    print(min(hold[n-1],carry[n-1]))

sol(N,K,A,B)




