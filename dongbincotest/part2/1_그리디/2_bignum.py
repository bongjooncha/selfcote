# N으로 몇개의 숫자를 입력받을지
# M으로 몇번 더할지
# K로 몇번까지 연속으로 더할지 정함

N, M, K = map(int,input().split())
num_list = list(map(int,input().split()))

num_list.sort(reverse=True)

ans = (num_list[0]*K + num_list[1])*(M//(K+1)) + num_list[0] * (M%(K+1))

print(ans)

# input값
# 5 8 3
# 2 4 5 4 6