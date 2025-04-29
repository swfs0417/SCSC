n, m = map(int, input().split())
p = set([input() for _ in range(n)])
q = set([input() for _ in range(m)])

r = p.intersection(q)

print(len(r))
print("\n".join(sorted(r)))
