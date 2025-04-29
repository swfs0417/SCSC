s = input()
sub = set()

for i in range(1, len(s) + 1):  # 문자열 길이
    for j in range(len(s) - i + 1):  # index
        sub.add(s[j : j + i])

print(len(sub))
