n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])

l, r = 0, houses[-1]
m = (l + r) // 2  # distance


def checkcount(m):
    setedplace = houses[0]
    setedcount = 1
    for i in houses[1:]:
        if i - setedplace >= m:
            setedplace = i
            setedcount += 1
    return setedcount


while l < r:
    if l == m:
        if checkcount(r) >= c:
            l += 1
            m = (l + r) // 2
        else:
            r -= 1
            m = (l + r) // 2
    # print(l, m, r)
    setedcount = checkcount(m)
    if setedcount >= c:
        l = m
        m = (l + r) // 2
    elif setedcount < c:
        r = m
        m = (l + r) // 2

    # print(setedcount)
# print(l, m, r)
print(m)
