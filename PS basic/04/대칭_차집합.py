n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a.symmetric_difference(b)))
