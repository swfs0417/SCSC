s = input()
b = list(input())

# while b in s:
#     s = s.replace(b, "")

result = []

for i in s:
    result.append(i)
    if len(result) >= len(b) and result[-len(b) :] == b:
        for _ in range(len(b)):
            result.pop()


print("".join(result) if result else "FRULA")
