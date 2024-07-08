import itertools

N = int(input().strip())

digi = list(str(N))

per = sorted(set(itertools.permutations(digi)))

print(sorted(list(itertools.permutations(digi))))