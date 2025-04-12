from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n, p = map(int, input().split())

pressed = [deque() for _ in range(6)]
result = 0

for _ in range(n):
    line, pret = map(int, input().split())
    while pressed[line - 1] and pressed[line - 1][-1] > pret:
        pressed[line - 1].pop()
        result += 1

    if (not pressed[line - 1]) or (pressed[line - 1] and pressed[line - 1][-1] != pret):
        pressed[line - 1].append(pret)
        result += 1


print(result)
