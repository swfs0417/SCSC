import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
s = [input() + " " + str(i) for i in range(n)]
result = sorted(s, key=lambda x: tuple(map(int, x.split()[::2])))
result = map(lambda x: " ".join(x.split()[:2]), result)
print("\n".join(result))
# print("\n".join(s))
