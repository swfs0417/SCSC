from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
q = deque()
for _ in range(n):
    line = input().split(" ")
    if line[0] == "push":
        q.append(int(line[1]))
    elif line[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif line[0] == "size":
        print(len(q))
    elif line[0] == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif line[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif line[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
