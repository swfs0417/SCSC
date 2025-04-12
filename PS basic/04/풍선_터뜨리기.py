from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

balloons = [[i, k] for i, k in zip(range(1, n + 1), map(int, input().split()))]
i = 0
while balloons:
    # print(i)
    i %= len(balloons)
    recent = balloons.pop(i)
    print(recent[0], end=" ")
    # print(i, recent[1], len(balloons))
    i += recent[1]
    if recent[1] > 0:
        i -= 1
