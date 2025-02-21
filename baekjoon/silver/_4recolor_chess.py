# https://www.acmicpc.net/problem/1018

# N, M = map(int,input().split())
# graph = [list(input()) for _ in range(N)]

# W = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]


# answer = 100
# for i in range(N-7):
#     for j in range(M-7):
#         for index, line in enumerate(graph[i:i+8]):
#             ans += sum(1 for x,y in zip(W[index],line[j:j+8]) if x!=y)
#         if ans > 32:
#             ans = 64 -ans
#         answer = min(ans,answer)
# print(answer)
            

import sys

input = sys.stdin.readline

N,M = map(int,input().strip().split())
maps = [list(input().strip()) for _ in range(N)]

ans_shit = [['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W'],
            ['W','B','W','B','W','B','W','B'],['B','W','B','W','B','W','B','W']]

def check(a,b):
    count = 0
    for row1, row2 in zip(a,b):
        for ele1, ele2 in zip(row1, row2):
            if ele1 == ele2:
                count += 1
    if count > 32:
        return 64-count
    else:
        return count
    
ans = 64
for i in range(N-7):
    for j in range(M-7):
        board = maps[i:i+8][j:j+8]
        if len(board)==0:
            print(i,j)
        ans = min(ans,check(ans_shit,board))
print(len(maps[0]),len(maps),i,j)
print(ans)
