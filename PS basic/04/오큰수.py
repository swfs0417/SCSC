n = int(input())
a = list(map(int, input().split()))
nge = [-1 for _ in range(n)]
q = []

for i in range(n):
    while q and a[q[-1]] < a[i]:
        nge[q.pop()] = a[i]
    q.append(i)

print(" ".join(map(str, nge)))
