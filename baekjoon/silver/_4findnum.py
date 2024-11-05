# https://www.acmicpc.net/problem/1920

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int,input().split()))

for i in m_list:
    if i in n_list:
        print(1)
        n_list.remove(i)
    else:
        print(0)