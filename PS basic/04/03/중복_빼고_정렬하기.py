n = int(input())
l = map(int, input().split())
print(*sorted(list(set(l))), sep=" ")
