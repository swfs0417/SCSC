import sys
from collections import deque
import re

input = lambda: sys.stdin.readline().rstrip()
a = deque()
while True:
    line = input()
    if line == ".":
        break
    for s in line:
        if s == "(":
            a.append("(")
        elif s == ")":
            if a and a[-1] == "(":
                a.pop()
            else:
                print("no")
                break
        elif s == "[":
            a.append("[")
        elif s == "]":
            if a and a[-1] == "[":
                a.pop()
            else:
                print("no")
                break
    else:
        if a:
            print("no")
        else:
            print("yes")
    a.clear()
