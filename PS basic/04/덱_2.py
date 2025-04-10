from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
deq = deque()
for _ in range(N):
    o = tuple(map(int, input().split()))
    if o[0] == 1:
        deq.appendleft(o[1])
    elif o[0] == 2:
        deq.append(o[1])
    elif o[0] == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif o[0] == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif o[0] == 5:
        print(len(deq))
    elif o[0] == 6:
        if deq:
            print(0)
        else:
            print(1)
    elif o[0] == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif o[0] == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)
