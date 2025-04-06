from collections import Counter

input()
a = Counter(input().split())
input()
x = input().split()
r = [str(a[i]) for i in x]
print(" ".join(r))
