n = int(input())
k = int(input())


def lessnum(s, n):
    acc = 0
    for i in range(1, n + 1):
        acc += min(s // i, n)

    return acc


l, r = 0, n * n
m = (l + r) // 2
while l < r:
    count = lessnum(m, n)
    if count >= k:
        r = m
        m = (l + r) // 2
    elif count < k:
        l = m if l != m else m + 1
        m = (l + r) // 2

print(m)
