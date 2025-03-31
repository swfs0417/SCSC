n = int(input())
result = [input() for _ in range(n)]
result = list(set(result))


def pivsort(li):
    if len(li) <= 1:
        return li
    m = li[len(li) // 2]
    ll, mm, rr = [], [], []
    for s in li:
        if s < m:
            ll.append(s)
        elif m < s:
            rr.append(s)
        else:
            mm.append(s)

    return pivsort(ll) + mm + pivsort(rr)


def cfstr(a, b):
    if len(a) < len(b):
        return True
    elif len(b) < len(a):
        return False
    else:
        return a < b


for s in pivsort(result):
    print(s)
