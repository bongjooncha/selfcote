n, m = map(int, input().split())
array = list(map(int, input().split()))
tasks = [tuple(map(int, input().split())) for _ in range(m)]

for task in tasks:
    i, j, k = task
    print(sorted(array[i-1:j] )[k-1])