n, k = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, max(a)  # noqa: E741
m = (l + r) // 2  # 점수차이
# k: 목표 지친사람 수 (maximize k)
# minimize m
# counter = 0
while l < r:
    # counter += 1
    tired = 0
    for i in range(len(a)):
        if (i != 0 and abs(a[i] - a[i - 1]) > m) or (
            i != len(a) - 1 and abs(a[i] - a[i + 1]) > m
        ):
            tired += 1
    if tired > k:
        l = m if l != m else m + 1
        m = (l + r) // 2
    elif tired < k:
        r = m
        m = (l + r) // 2
    else:
        r -= 1
        m = (l + r) // 2

print(m)
