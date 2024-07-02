# N = int(input())
# numbs = [int(input()) for _ in range(N)]
numbs = [3,2,5]

answers = [[1,0] for _ in range(41)]
answers[1] = [0, 1]

for i in range(2,max(numbs)):
    answers[i][0] = answers[i-1][0] + answers[i-2][0]   
    answers[i][1] = answers[i-1][1] + answers[i-2][1]   

print(answers)