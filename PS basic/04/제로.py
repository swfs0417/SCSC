import sys

input = lambda: sys.stdin.readline().rstrip()

stack = []
k = int(input())

for _ in range(k):
    i = int(input())
    if i != 0:
        stack.append(i)
    else:
        stack.pop()

print(sum(stack))
