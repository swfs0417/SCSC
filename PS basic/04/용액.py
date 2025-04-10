import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))

minimum = (2000000000, -1, -1)


def calc(st):
    diff = 2000000000
    to = -1
    l, r = st + 1, n
    m = (l + r) // 2
    while l < r:
        temp = a[st] + a[m]
        if abs(temp) < abs(diff):
            diff = temp
            to = m

        if temp < 0:
            l = m + 1
            m = (l + r) // 2
        elif temp > 0:
            r = m
            m = (l + r) // 2
        else:
            break

    return a[st], a[to], abs(diff)


for s in range(n):
    st, to, diff = calc(s)
    # print(st, to, diff)
    # print(minimum[0])
    if diff <= minimum[0]:
        minimum = (diff, st, to)

print(*minimum[1:])
