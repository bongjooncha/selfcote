# https://www.acmicpc.net/problem/10451

import sys
input = sys.stdin.readline

N = int(input())

def solv(numb,lists):
    visited = [False] * (numb+1)
    ans = 0
    perm = [0]+lists
    for start in range(1,numb+1):
        if not visited[start]:
            current = start
            while not visited[current]:
                visited[current] = True
                current = perm[current]
            ans += 1
    return ans



for _ in range(N):
    numb = int(input())
    lists = list(map(int,input().split()))
    print(solv(numb,lists))
