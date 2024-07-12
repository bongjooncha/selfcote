from itertools import combinations

N = int(input())
a_list = list(map(int,input().split()))
a_list.remove(0)
a_list.sort()

# comb는 무작위
for comb in combinations(a_list,N):
    new = []
    for i in range(1,len(comb)+1):
        for make in combinations(comb,i):
            new.append(sum(make))
    new.sort()
    if a_list == new:
        print(comb)