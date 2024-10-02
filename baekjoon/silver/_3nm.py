import sys

def backtrack(sequence, used):
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return
    for i in range(n):
        if not used[i]:
            used[i] = True
            sequence.append(li[i])
            backtrack(sequence, used)
            sequence.pop()
            used[i] = False


n, m = map(int, sys.stdin.readline().split())
li = list(map(int, sys.stdin.readline().split()))
li.sort()
used = [False] * n
backtrack([], used)

