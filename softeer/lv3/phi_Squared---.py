#https://softeer.ai/practice/7697

N = int(input())
microbes = list(map(int,input().split()))

print(sum(microbes))
microbes = [[index+1, microbe] for index, microbe in enumerate(microbes)]


while len(microbes) > 1:
    i = 0
    while i < len(microbes):
        current_size = microbes[i][1]
        if i == 0 and current_size >= microbes[i+1][1]:
            microbes[i][1] += microbes[i+1][1]
            microbes.pop(i+1)
        elif i > 0 and i < len(microbes)-1:
            if current_size >= microbes[i+1][1]:
                microbes[i][1] += microbes[i+1][1]
                microbes.pop(i+1)
            if current_size >= microbes[i-1][1]:
                microbes[i][1] += microbes[i-1][1]
                microbes.pop(i-1)
                i -= 1
        elif i == len(microbes)-1 and current_size >= microbes[i-1][1]:
                microbes[i][1] += microbes[i-1][1]
                microbes.pop(i-1)
        i += 1
print(microbes[0][0])