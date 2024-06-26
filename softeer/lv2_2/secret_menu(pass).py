# https://softeer.ai/practice/6269
M, N, K = map(int, input().split())

secret = input()
user = input()

if secret in user:
    print("secret")
else: print("normal")