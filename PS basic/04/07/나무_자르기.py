_, t = map(int, input().split())
h = list(map(int, input().split()))
# print(list(h))
l, r = 0, max(h)  # noqa: E741
m = (l + r) // 2
counter = 0
while l + 1 < r and counter < 10:
    s = 0
    for i in h:
        cut = i - m
        if cut > 0:
            s += cut
    # s = sum([i-m for i in h if i - m > 0])
    # print(s)
    if s > t:
        l = m  # noqa: E741
        m = (l + r) // 2
    elif s < t:
        r = m
        m = (l + r) // 2
    else:
        break
    # counter += 1

print(m)
