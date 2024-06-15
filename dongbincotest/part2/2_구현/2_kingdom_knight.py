# 8x8 체스판
# 체스말의 위치가 주어짐
# 체스말이 갈수 있는 칸을 추력

A = input()


if A[0] == "a" or A[0] == "h":
    ans = 2
elif A[0] == "b" or A[0] == "g":
    ans = 3
else:
    ans = 4

if A[1] == "1" or A[1] == "8":
    ans *= 1

elif A[1] == "2" or A[1] == "7":
    ans = ans * 2 -1
else:
    ans = ans * 2

print(ans)