# https://www.acmicpc.net/problem/1015
import sys

input = sys.stdin.readline

N = int(input())
LIST = list(enumerate(map(int,input().split())))

sorted_with_order = [(item[0], idx) for idx, item in enumerate(sorted(LIST, key=lambda x: x[1]))]

ans = [x[1] for x in sorted(sorted_with_order)]

print(*ans)


'''
1. 입력받은 수를 순서대로 정렬
2. 정렬된 번호를 추가
3. 원래 순서로 되돌림
4. 정렬된 번호 출력
'''