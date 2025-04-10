n, k = map(int, input().split())
y = list(range(1, n + 1))


def getidx(idx):
    idx = idx % len(y)


result = []
idx = 0
for i in range(1, n + 1):
    # print(y)
    idx += k - 1
    idx = idx % len(y)
    result.append(str(y.pop(idx)))

print(f"<{', '.join(result)}>")
