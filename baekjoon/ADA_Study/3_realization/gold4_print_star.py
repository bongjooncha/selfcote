# https://www.acmicpc.net/problem/10993

'''
짝수는 역배열, 홀수는 정배열. => 재귀로 풀기
(*의 갯수와 " "의 갯수를 고려 했을때 직사각형(엄밀히 따지면 사다리꼴)이라고 생각 가능.
다만 *이 찍히는 위치만 다를뿐(각 줄의 마지막부분은 생략))

----- 높이 ------
1:1, 2:1*2+1=3, 3:3*2+1=7, 4: 7*2+1=15 ....
----- 넓이 ------
밑변(가장 긴변의 길이) = 1+2*(높이-1)

-----------
짝수인 경우 위가 가장 넓음. 첫줄 이후 바로 재귀 실행.
재귀 실행 이후 이어서 좁히기

-----------
홀수의 경우 위가 가장 좁음. 가운데줄((높이+1)/2) 부터 재귀 시작
마지막 줄까지 이어서 넓히기
-----------
'''
import sys
input = sys.stdin.readline

N = int(input())

def build(n):
    if n == 1:
        return ["*"]

    child = build(n - 1) 
    h_c, w_c = len(child), len(child[0]) # 자식 높이·너비
    h = h_c * 2 + 1                      # 이번 높이
    w = w_c + 2 * (h_c + 1)              # 이번 너비(= 2^(n+1)-3)

    canvas = [" " * w for _ in range(h)] # 공백으로 채워 둔 도화지
    lines = list(canvas)                 # 문자열은 불변이라 list로 복사

    if n % 2:               # ▲(정삼각형)
        mid = w // 2
        # ▲ 양 옆 변
        for i in range(h):
            if i == h - 1:                 # 밑변
                lines[i] = "*" * w
            elif i == 0:                   # 꼭짓점(한 개만)
                lines[i] = lines[i][:mid] + "*" + lines[i][mid + 1:]
            else:
                left = mid - i
                right = mid + i
                lines[i] = (
                    lines[i][:left] + "*" +
                    lines[i][left + 1:right] + "*" +
                    lines[i][right + 1:]
                )
        # 안쪽 역삼각형(▼) 삽입
        offset = (w - w_c) // 2          # 좌우 여백
        base   = h_c                     # 삽입할 시작 행
        for i in range(h_c):
            lines[base + i] = (
                lines[base + i][:offset] +
                child[i] +
                lines[base + i][offset + w_c:]
            )
    else:                   # ▼(역삼각형)
        # ▼ 양 옆 변 + 윗변
        for i in range(h):
            if i == 0:                      # 윗변
                lines[i] = "*" * w
            elif i == h - 1:                # 꼭짓점(한 개만)
                mid = w // 2
                lines[i] = lines[i][:mid] + "*" + lines[i][mid + 1:]
            else:
                left = i
                right = w - 1 - i
                lines[i] = (
                    lines[i][:left] + "*" +
                    lines[i][left + 1:right] + "*" +
                    lines[i][right + 1:]
                )
        # 안쪽 정삼각형(▲) 삽입
        offset = (w - w_c) // 2          # 좌우 여백
        base   = 1                       # 삽입할 시작 행
        for i in range(h_c):
            lines[base + i] = (
                lines[base + i][:offset] +
                child[i] +
                lines[base + i][offset + w_c:]
            )

    return lines

def solve():
    picture = build(N)
    print("\n".join(s.rstrip() for s in picture))

if __name__ == "__main__":
    solve()