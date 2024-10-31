# https://www.acmicpc.net/problem/1181
import sys

input = sys.stdin.readline

n = int(input())
words = {input().strip() for _ in range(n)}
sorted_words = sorted(words, key=lambda x: (len(x), x))

for word in sorted_words:
    print(word)