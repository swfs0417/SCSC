n = int(input())
incar = [input() for _ in range(n)]
outcar = [input() for _ in range(n)]

i, o = 0, 0
r = 0
passed = set()
# print(*list(zip(incar, outcar)), sep="\n")
while i < n and o < n:
    # print(i, o)
    if incar[i] in passed:
        i += 1
    elif incar[i] == outcar[o]:
        i += 1
        o += 1
    else:
        passed.add(outcar[o])
        r += 1
        o += 1

print(r)
