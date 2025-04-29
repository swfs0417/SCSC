from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

line = deque()
pair = n - 1
for _ in range(n):
    next = int(input())
    print(line, next, pair)
    while line and line[-1] < next:
        line.pop()
        pair += 1

    # pair += len(line)
    line.append(next)

print(pair)
