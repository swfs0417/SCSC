import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    minhq = []
    maxhq = []
    l = 0
    k = int(input())
    for _ in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == "I":
            heapq.heappush(minhq, n)
            heapq.heappush(maxhq, -n)
            l += 1
        else:
            if n == 1 and maxhq:
                heapq.heappop(maxhq)
                l -= 1
            elif n == -1 and minhq:
                heapq.heappop(minhq)
                l -= 1

        if l == 0:
            minhq, maxhq = [], []

    if len(minhq) > 0:
        print(-min(maxhq), min(minhq))
    else:
        print("EMPTY")
