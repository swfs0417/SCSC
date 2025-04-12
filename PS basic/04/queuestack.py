from collections import deque

n = int(input())
a = map(int, input().split())
b = map(int, input().split())
q = deque([j for i, j in zip(a, b) if not i])
# print(a, b)
m = int(input())
c = list(map(int, input().split()))
result = []
for i in c:
    # print(b)
    q.appendleft(i)
    result.append(str(q.pop()))

print(" ".join(result))
