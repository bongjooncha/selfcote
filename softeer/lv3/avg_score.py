# https://softeer.ai/practice/6294

N, K = map(int, input().split())
scores = list(map(int, input().split()))
ranges = [list(map(int,input().split())) for _ in range(K)]

for range in ranges:
    ans = sum(scores[range[0]-1:range[1]])/(range[1]-range[0]+1)
    print(f"{ans:.02f}")