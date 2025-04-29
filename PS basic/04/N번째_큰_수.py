import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
hq = []

for _ in range(n):
    for i in map(int, input().split()):
        heapq.heappush(hq, i)
    while len(hq) > n:
        heapq.heappop(hq)
print(heapq.heappop(hq))
