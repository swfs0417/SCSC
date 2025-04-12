from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):
    cmd = input()
    n = int(input())
    x = input().strip("[").strip("]")
    if x:
        x = deque(x.split(","))
    else:
        x = deque([])
    reverse = False
    for c in cmd:
        if c == "R":
            reverse = not reverse
        elif c == "D":
            if x:
                if reverse:
                    x.pop()
                else:
                    x.popleft()
            else:
                print("error")
                break
    else:
        x = list(x)
        print(f"[{','.join(x[::-1])}]" if reverse else f"[{','.join(x)}]")
