import sys

input = lambda: sys.stdin.readline().rstrip()

input()
a = set(input().split())
input()
x = input().split()
r = [str(int(i in a)) for i in x]

print("\n".join(r))
