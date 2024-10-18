# https://www.acmicpc.net/problem/15649
from itertools import permutations
N, M = map(int, input().split())

num_list = list(range(1,N+1))		#순차 리스트 생성

for i in permutations(num_list,M):	#조건에 맞게 순열 생성
    for element in i:
        print(element, end=' ')		#출력
    print()