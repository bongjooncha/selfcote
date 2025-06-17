# https://www.acmicpc.net/problem/2670

'''
N개의 실수 존재. 1개 이상의 연속된 수들의 곱이 되대가 되는 부분 찾기
이전의 값이 1이상일 경우 곱하는게 이득
ans 유지한 상태로 이전 상태가 1이상일 경우 다음 수와 지속해서 곱하기. 아닐 경우 Prev 버리기
'''

import sys

input = sys.stdin.readline

N = int(input())
LISTS = []
for i in range(N):
    LISTS.append(float(input()))

def sol(n,lists):
    ans = lists[0]
    priv = lists[0]

    for i in range(1,n):
        if priv >= 1:
            priv = lists[i]*priv
            ans = max(ans,priv)
        else:
            priv = lists[i]
            ans= max(ans,priv)

    print(f"{ans:.3f}")

sol(N,LISTS)