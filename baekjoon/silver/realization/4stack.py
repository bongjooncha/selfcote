# https://www.acmicpc.net/problem/10828

import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = sys.stdin.readline()

    if "push" in command:
        stack.append(int(command[5:]))

    elif "pop" in command:
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop()
            print(a)

    elif "size" in command:
        print(len(stack))

    elif "empty" in command:
        if len(stack) == 0:
            print(1)
        else: print(0)

    else:
        if len(stack) == 0:
            print(-1)
        else: print(int(stack[-1]))

