# https://www.acmicpc.net/problem/1021

n, m = map(int, input().split())
nums = list(range(1, n+1))
keys = list(map(int, input().split()))

ans = 0

for i in keys:
    index = nums.index(i)
    if index <= len(nums) // 2:
        ans += index
        nums = nums[index+1:] + nums[:index]
    
    else:
        ans += len(nums)-index
        nums = nums[index+1:] + nums[:index]
        
print(ans)