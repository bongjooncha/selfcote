# https://www.acmicpc.net/problem/1065

n = int(input())

if n <= 99:
    print(n)
elif n<1000:
    ans = 99
    for i in range(100,n+1):
        nums = str(i)
        if (int(nums[0]) - int(nums[1])) == (int(nums[1]) - int(nums[2])):
            ans +=1
    print(ans)
else:
    print(144)


    """
    풀이
    각 자리수를 비교, n은 1000이하
    99까지는 자신까지 모두 한 수
    111,123,135,
    """