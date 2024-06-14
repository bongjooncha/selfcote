# https://softeer.ai/practice/6282
# 1이 장애물, 0이 도로, 정사각형으로 주어짐
# 장애물 수를 오름차순으로 출력

N = int(input())
road = [list(map(int,input().split())) for _ in range(N)]

print(road)