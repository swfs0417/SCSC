n, k = map(int, input().split())
a = list(map(int, input().split()))


def gettired(score):
    acc = 0
    for i in range(n):
        if (i != 0 and abs(a[i] - a[i - 1]) > score) or (
            i != len(a) - 1 and abs(a[i] - a[i + 1]) > score
        ):
            acc += 1
    return acc


l, r = 0, max(a)
m = (l + r) // 2

while l < r:
    t = gettired(m)
    # print(l, m, r, t)
    if t > k:
        l = m if l != m else m + 1
        m = (l + r) // 2
    elif t <= k:
        r = m
        m = (l + r) // 2

print(m)
