#https://softeer.ai/practice/7703
# N은 5e5이하. 첫줄에 N 주어짐. 둘째 줄부터 문자열 S,T 가 공백으로 주어짐. S,T는 같고, S에서 x(X)가 등장 하는 위치와 동일한 위치에 있는 T의 알벳 혹은 숫자를 출력

import sys
# 전체 입력을 lines 리스트에 읽습니다.
# lines = sys.stdin.readlines()

N = int(input())  # 첫 번째 줄에는 테스트 케이스 수가 포함되어 있습니다.
ans = ''

for _ in range(N):  # 첫 번째 줄(테스트 케이스 수) 건너뛰기
    word1, word2 = input().upper().split()
    index = word1.index("X")
    ans += word2[index]

print(ans)