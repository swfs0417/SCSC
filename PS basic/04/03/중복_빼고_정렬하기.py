n = int(input())
l = map(int, input().split())  # noqa: E741
print(*sorted(list(set(l))), sep=" ")
