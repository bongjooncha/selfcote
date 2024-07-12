from itertools import combinations

N = int(input())
a_list = list(map(int,input().split()))

ans = []
a_list.remove(0)

while len(ans) < N:
    for i in range(1,len(ans)+1):
        for comb in combinations(ans,i):
            try:
                a_list.remove(sum(comb))
            except ValueError:
                pass
    ans.append(min(a_list))
    a_list.remove(min(a_list))


print(' '.join(str(i) for i in ans))