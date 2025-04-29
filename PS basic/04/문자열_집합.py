n, m = map(int, input().split())
s = set([input() for _ in range(n)])

r = 0
for _ in range(m):
    t = input()
    if t in s:
        r += 1

print(r)
