# https://softeer.ai/practice/6280

N = int(input())

points = 2

for i in range(N):
    points += points-1

print(points*points)


# 2
# 3
# 5
# 9
