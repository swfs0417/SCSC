from collections import Counter


input()
a = Counter(map(int, input().split()))
b = map(int, input().split())
levelcut = {0: 0}
nowarea = 1
possible = 0
target = 1
for lev in sorted(a.keys()):
    possible += a[lev]
    if possible >= target:
        levelcut[lev] = nowarea
        nowarea += 1
        target = 3 * nowarea * (nowarea - 1) + 1
r = []

for lev in b:
    temp = 0
    for i in levelcut.keys():
        if i > lev:
            r.append(levelcut[temp])
            break
        temp = i
    else:
        r.append(levelcut[temp])
print(" ".join(map(str, r)))
