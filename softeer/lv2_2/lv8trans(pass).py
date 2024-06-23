# https://softeer.ai/practice/6283
accel = list(map(int,input().split()))

if accel == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif accel == [8,7,6,5,4,3,2,1]:
    print("descending")
else:
    print("mixed")