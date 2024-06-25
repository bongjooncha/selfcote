#https://softeer.ai/practice/7703
N = int(input())

word_list = [list(input().split()) for _ in range(N)]

answer = []
for word in word_list:
    for i in range(len(word[0])):
        if word[0][i] == "x" or word[0][i] == "X":
            print(word[1][i].upper(), end ="")