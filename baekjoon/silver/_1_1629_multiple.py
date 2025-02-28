# https://www.acmicpc.net/problem/1629
# silver1
# gready(math)

import sys 

input = sys.stdin.readline

A, B, C = map(int, input().strip().split())

def po(a,b,c):
    if b ==1:
        return a % c
    
    tem = pow(a,b //2,c)
    if b % 2 == 0:
        return (tem * tem) % c
    else:
        return (tem*tem)*a % c

print(po(A,B,C))