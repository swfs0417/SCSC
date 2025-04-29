import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()
minheap = []

n = int(input())

for _ in range(n):
    o = int(input())
    if o:
        heapq.heappush(minheap, o)
    else:
        if minheap:
            print(heapq.heappop(minheap))
        else:
            print(0)
