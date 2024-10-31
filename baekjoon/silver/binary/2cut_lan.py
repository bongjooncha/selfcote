# https://www.acmicpc.net/problem/1654

import sys

input = sys.stdin.readline

k, n = map(int,input().split())
lens = [int(input()) for _ in range(k)]

ans = sum(lens) // n

