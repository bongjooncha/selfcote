# https://www.acmicpc.net/problem/17952

'''
제한시간 2초, 메모리 제한 256MB

가장 최근에 나온대로 순서 -> 새로운 과제가 나오면 중단하고 새로운거 시작 -> 이후 이전에 하던거 이어서

새로나온 과제가 있다면 그 과제에서 시간 -1
없다면 가장 위에 있는 과제 시간 -1 => 0이 되면 제거 후 점수로 치환

'''

import sys

input = sys.stdin.readline

N = int(input())
ASSIGNS = [list(map(int,input().split())) for _ in range(N)]

def sol(assigns):
    ans = 0
    stack = []
    for assign in assigns:
        if assign[0] == 1:
            _,A,T = assign
            stack.append((A,T))

        if stack:
            score, time = stack[-1]
            time -= 1
            if time == 0:
                ans += score
                stack.pop()
            else:
                stack[-1] = (score, time)

    return ans

print(sol(ASSIGNS))

