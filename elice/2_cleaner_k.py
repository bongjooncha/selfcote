def process_tasks(array, tasks):
    for task in tasks:
        i, j, k = task
        print(sorted(array[i-1:j] )[k-1])


# 입력
n, m = map(int, input().split())
array = list(map(int, input().split()))
tasks = [tuple(map(int, input().split())) for _ in range(m)]

# 작업 처리 및 출력
results = process_tasks(array, tasks)
