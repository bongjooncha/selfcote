#https://softeer.ai/practice/7628

# 난로의 반지름 길이가 연탄의 반지름 길의 배수여야함
# n개의 집에 난로 반지름이 주어짐. 산타가 최대한 많은 집에 연탄 배달할 수있게 만들어야함
# 단 난로의 반지름과 연탄의 반지름은 정수 + 2이상

# 입력 => 첫줄에 N, 둘째 줄에 각집에 있느 난로의 반지름 길이 공백으로 주어짐

N = int(input())
radi = list(map(int,input().split()))

max_ans = 1
for i in range(2,max(radi)+1):
    ans = 0
    for j in radi:
        if j % i == 0:
            ans +=1
    max_ans = max(max_ans,ans)
print(max_ans)