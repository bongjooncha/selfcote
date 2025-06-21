# https://www.acmicpc.net/problem/2096

'''
N개의 줄 존재. 1-9 작성됨.

가운데를 제외한 사이드는 반대 사이드에 갈 수 없음.(가운데는 모두 가능)
따라서 사이드일때와 가운데인 경우 두칸 생성 필요.
'''

import sys

input = sys.stdin.readline

N = int(input())
NUMS = []
for _ in range(N):
    NUMS.append(list(map(int,input().split())))

def sol(nums):
    max_ans = [0,0,0]
    min_ans = [0,0,0]
    for num in nums:
        copy_max_ans = max_ans.copy()
        copy_min_ans = min_ans.copy()
        max_ans[0] = num[0]+max(copy_max_ans[0],copy_max_ans[1])
        max_ans[1] = num[1]+max(copy_max_ans)
        max_ans[2] = num[2]+max(copy_max_ans[1],copy_max_ans[2])

        min_ans[0] = num[0]+min(copy_min_ans[0],copy_min_ans[1])
        min_ans[1] = num[1]+min(copy_min_ans)
        min_ans[2] = num[2]+min(copy_min_ans[1],copy_min_ans[2])


    return max(max_ans),min(min_ans)

ans = sol(NUMS)

print(f'{ans[0]} {ans[1]}')
    