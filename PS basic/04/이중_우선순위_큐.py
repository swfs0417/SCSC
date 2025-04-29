import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    hq = []
    k = int(input())
    for _ in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == "I":
            heapq.heappush(hq, n)
        else:
            if n == 1 and hq:
                heapq._heapify_max(hq)
                heapq.heappop(hq)
            elif n == -1 and hq:
                heapq.heapify(hq)
                heapq.heappop(hq)
    if len(hq) > 2:
        print(max(hq), heapq.heappop(hq))
    else:
        print("EMPTY")
