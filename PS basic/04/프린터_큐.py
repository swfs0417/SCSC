from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

case = int(input())
for _ in range(case):
    n, m = map(int, input().split())
    line = list(map(int, input().split()))
    queue = deque([(i, line[i]) for i in range(n)])
    result = []
    while queue:
        while max(queue, key=lambda x: x[1])[1] > queue[0][1]:
            queue.append(queue.popleft())
        result.append(queue.popleft())
    print(result.index((m, line[m])) + 1)
