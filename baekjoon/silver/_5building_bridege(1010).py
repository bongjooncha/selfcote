from math import factorial

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(int(factorial(b)/(factorial(a)*factorial(b-a))))