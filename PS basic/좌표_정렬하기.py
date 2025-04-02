import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
a = sorted(a)
for s in a:
    print(*s)
