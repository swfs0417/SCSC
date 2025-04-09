from collections import deque

line = input().replace("()", "0")

a = deque()
result = 0
for s in line:
    # print(a, result)
    if s == "(":
        a.append(1)
    elif s == ")":
        a.pop()
        result += 1
    elif s == "0":
        result += len(a)

print(result)
