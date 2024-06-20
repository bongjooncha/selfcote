#https://softeer.ai/practice/6266

N, M = map(int, input().split())
names = [input() for i in range(N)]
names.sort()
times = [list(input().split()) for _ in range(M)]

for time in times:
    time[1] = int(time[1])
    time[2] = int(time[2])

for index, name in enumerate(names):
    print(f"Room {name}:")
    ans = [9, 18]
    for time in times:
        if time[0] == name:
            if time[1] in ans:
                ans.remove(time[1])
            else:
                ans.append(time[1])
            if time[2] in ans:
                ans.remove(time[2])
            else:
                ans.append(time[2])
    ans.sort()

    if ans == []:
        print("Not available")
    else:
        print(f"{int(len(ans)/2)} available:")
        for i in range(int(len(ans)/2)):
            print(f"{ans[i*2]:02}-{ans[i*2+1]:02}")

    # 마지막 요소인 경우에만 "-----" 출력
    if index == len(names) - 1:
        break
    print("-----")
