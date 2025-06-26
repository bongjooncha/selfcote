# https://www.acmicpc.net/problem/2641

'''
약간의 순서나열 변환만으로 가능한지 확인.
이후 뒤집어보고 이게 가능한지 확인.

이때 정답지를 모두 만든뒤 여기에 해당하는게 있는지 확인.

N =< 100, COUNT <= 50

시간제한 1초, 메모리 제한 128MB
'''

import sys

input = sys.stdin.readline

LENGTH = int(input())
BASIC = list(map(int,input().split()))

N = int(input())
POLYS = [list(map(int, input().split())) for _ in range(N)]

#순서 변경 함수
def rotate_poly(poly,length):
    rotated_polys = [poly[i:]+poly[:i] for i in range(length)]
    return rotated_polys

# 뒤집는 함수
def rev_poly(poly):
    dic_map = {1:3, 2:4, 3:1, 4:2}
    rev_poly = [dic_map[num] for num in reversed(poly)]
    return rev_poly

# 정답지 완성하는 함수
def answer_sheet(basic, length):
    rotated_polys = rotate_poly(basic, length)
    reverse_poly = rev_poly(basic)
    reversed_rotated_polys = rotate_poly(reverse_poly, length)
    ans_sheet = rotated_polys + reversed_rotated_polys
    return ans_sheet

def sol(ans_sheet, polys):
    ans = []
    for poly in polys:
        if poly in ans_sheet:
            ans.append(poly)
    
    print(len(ans))
    for i in ans:
        print(*i)

ANSWER_SHEET = answer_sheet(BASIC,LENGTH)
sol(ANSWER_SHEET,POLYS)
    


