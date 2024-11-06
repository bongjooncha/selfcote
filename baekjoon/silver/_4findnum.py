# https://www.acmicpc.net/problem/1920

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int,input().split()))

for i in m_list:
    start, end = 0,n-1
    a = False

    while start <= end:
        mid = (end + start) // 2
        if i > n_list[mid]:
            start = mid +1
        elif i == n_list[mid]:
            a = True
            print(1)
            break
        else:
            end = mid -1
    if a is not True: print(0)
    


# N = int(input())
# A = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
# M = int(input())
# arr = list(map(int, input().split()))

# for num in arr:				# arr의 각 원소별로 탐색
#     print(1) if num in A else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력