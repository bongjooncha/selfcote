# https://www.acmicpc.net/problem/4673

num_set = {i for i in range(1,10001)}
self_num = set()

for i in range(10001):
    for j in str(i):
        i += int(j)
    self_num.add(i)

ans = list(num_set - self_num)
ans.sort()
for i in ans:
    print(i)