# https://softeer.ai/practice/6268/talk

T = int(input())
cases = [list(input().split()) for _ in range(T)]

display = {
'0': [True, True, True, False, True, True, True],
"1":[False, False, True, False, False, True, False],
'2':[True, False, True, True, True, False, True],
'3':[True, False, True, True, False, True, True],
'4':[False, True, True, True, False, True, False],
'5':[True, True, False, True, False, True, True],
'6':[True, True, False, True, True, True, True],
'7':[True, True, True, False, False, True, False],
'8':[True, True, True, True, True, True, True],
'9': [True, True, True, True, False, True, True],
"":[False, False, False, False, False, False, False]}

for case in cases:
    first = ['','','','','']
    second = ['','','','','']
    # 숫자 전광판화 작업
    for i in range(len(case[0])):
        first[-len(case[0])+i] = case[0][i]    
    for i in range(len(case[1])):
        second[-len(case[1])+i] = case[1][i]
    
    # 확인작업 시작
    ans = 0
    for i in range(5):
        for j in range(7):
            if display[first[i]][j] != display[second[i]][j]:
                ans += 1
    print(ans)
        