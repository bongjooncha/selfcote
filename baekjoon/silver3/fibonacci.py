N = int(input())
numbs = [int(input()) for _ in range(N)]

answers = [[1,0] for _ in range(41)]
answers[1] = [0, 1]

for i in range(2,max(numbs)+1):
    answers[i][0] = answers[i-1][0] + answers[i-2][0]   
    answers[i][1] = answers[i-1][1] + answers[i-2][1]  

for num in numbs:
    print(answers[num][0], answers[num][1])

# 0 => 1 0
# 1 => 0 1
# 2 => 1 0(0) + 0 1(1) => 1 1
# 3 => 1 1(2) + 0 1(1) => 1 2
# 4 => 1 2(3) + 1 1(2) => 2 3
# 5 => 1 2(3) + 2 3(4) => 3 5