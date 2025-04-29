from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n, k = map(int, input().split())
insertlist = deque()
namelist = {}
result = 0
for _ in range(n):
    print(namelist, result)
    name = input()
    insertlist.append(len(name))
    if len(name) in namelist:
        namelist[len(name)].append(name)
    else:
        namelist[len(name)] = deque([name])

    if len(insertlist) > k + 1:
        namelist[insertlist.popleft()].popleft()

    result += len(namelist[len(name)]) - 1
# print(namelist, result)
print(result)
