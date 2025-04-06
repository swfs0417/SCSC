k, n = map(int, input().split())
ll = [int(input()) for _ in range(k)]

l, r = 0, max(ll)
mid = (l + r) // 2
while l + 1 < r:
    amount = 0
    for i in ll:
        amount += i // mid
    if amount >= n:
        l = mid
        mid = (l + r) // 2
    elif amount < n:
        r = mid
        mid = (l + r) // 2
ramm = 0
for i in ll:
    ramm += i // r
print(r if ramm == n else mid)
