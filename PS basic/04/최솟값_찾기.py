from collections import deque
import heapq

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = []

q = []

for i in range(n):
    # print(q)
    heapq.heappush(q, (a[i], i))
    m = heapq.heappop(q)
    while m[1] < i - k + 1:
        m = heapq.heappop(q)
    result.append(m[0])
    heapq.heappush(q, m)


print(" ".join(map(str, result)))
