# https://softeer.ai/practice/6268

N = int(input())
displays = [list(input().split()) for _ in range(N)]

leds = {
    "" :[False, False, False, False, False, False, False],
    "0":[True, True, True, False, True, True, True],
    "1":[False, False, True, False, False, True, False],
    "2":[True, False, True, True, True, False, True],
    "3":[True, False, True, True, False, True, True],
    "4":[False, True, True, True, False, True, False],
    "5":[False, False, False, False, True, False, False],
    "6":[True, True, False, True, True, True, True],
    "7":[True, True, True, False, False, True, False],
    "8":[True, True, True, True, True, True, True],
    "9":[True, True, True, True, False, True, True],
}

for display in displays:
    a = [""]*8
    b = [""]*8
    for i in range(-1, -len(display[0]) -1, -1):
        a[i] = display[0][i]
    for i in range(-1, -len(display[1])-1, -1):
        b[i] = display[1][i]

