import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
a = deque([int(input()) for _ in range(n)])
q = deque()
s = []

for i in range(1, n + 1):
    q.append(i)
    s.append("+")
    while q and q[-1] == a[0]:
        a.popleft()
        q.pop()
        s.append("-")

if a:
    print("NO")
else:
    print("\n".join(s))
