import sys

input = lambda: sys.stdin.readline().rstrip()


t = int(input())

for _ in range(t):
    stack = []
    line = input()
    for s in line:
        if s == "(":
            stack.append(1)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")
