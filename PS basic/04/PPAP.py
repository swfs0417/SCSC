s = input()
b = list("PPAP")

# while b in s:
#     s = s.replace(b, "")

result = []

for i in s:
    result.append(i)
    if len(result) >= len(b) and result[-len(b) :] == b:
        for _ in range(len(b)):
            result.pop()
        result.append("P")
# print(result)

print("PPAP" if result == ["P"] else "NP")
