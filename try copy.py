import itertools

N = int(input().strip())

digi = list(str(N))
per = sorted(set(itertools.permutations(digi)))

for i in per:
    p_num = int(''.join(i))
    if p_num > N:
        print(p_num)
        break
   