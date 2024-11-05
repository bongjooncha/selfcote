# https://www.acmicpc.net/problem/1181
import sys

input = sys.stdin.readline

n = int(input())
words_set = {input().strip() for _ in range(n)}

words = list(words_set)
words.sort()
words.sort(key = lambda x : len(x))

for word in words:
    print(word)