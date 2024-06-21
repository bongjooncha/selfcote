# X에 사용가능한 연산 4개.
# 5,3,2로 나누거나 1 빼기

X = int(input())

d = [0]*(X+1)

for i in range(2,X+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
print(d)
print(d[X])