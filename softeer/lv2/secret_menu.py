# https://softeer.ai/practice/6269

#M개의 버튼 조작으로 순서대로 누르면 비밀메뉴 식권 발매
#K의 순서가 N에 포함되어 있음 secret, 아님 normal

# 비밀 메뉴 조작법 M개의 버튼으로 조작, 사용자는 N개의 버튼 주어짐, 자판기에 k개의 버튼
M, N, K = map(int,input().split())
menual = input()
buttons = input()

if menual in buttons:
    print("secret")
else: print("normal")