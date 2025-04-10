import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
u = sorted([int(input()) for _ in range(N)])
s = set()
for x in u:
    for y in u:
        s.add(x + y)
k = False
for i in range(N - 1, -1, -1):
    if k:
        break
    for j in range(i, -1, -1):
        if u[i] - u[j] in s:
            print(u[i])
            k = True
            break


# print(s)
# idk
