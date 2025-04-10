N, M, R = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
d = sorted(list(set([abs(a[x] - a[y]) for x in range(N) for y in range(x + 1, N)])))
N = len(d)

maxarea = 0
for h in b:
    l, r = 0, N
    m = (l + r) // 2
    while l < r:
        temp = h * d[m] / 2
        if temp > R:
            r = m
            m = (l + r) // 2
        elif temp <= R:
            if maxarea < temp:
                maxarea = temp
            l = m if m != l else m + 1
            m = (l + r) // 2
    if maxarea == R:
        break

print(maxarea if maxarea else -1)
