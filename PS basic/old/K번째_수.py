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


_, t = map(int, input().split())

print(pivsort(list(map(int, input().split())))[t - 1])
