n = int(input())
s = list(map(int, input().split()))

s2 = sorted(set(s))
d = {}
for i in range(len(s2)):
    d[s2[i]] = i
print(" ".join(map(lambda x: str(d[x]), s)))
