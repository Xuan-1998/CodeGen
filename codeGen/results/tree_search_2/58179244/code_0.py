import sys

def solve():
    n = int(input())
    s = input()

    dp = {}
    for i in range(n):
        c = s[i]
        if (i, c) not in dp:
            dp[(i, c)] = 1 + min(dp.get((i-1, d), float('inf')) for d in 'RGB' if d != c)
    r = dp.get((n-1, s[-1]), -1)

    # construct the diverse garland
    t = []
    prev_c = None
    for i in range(n):
        c = s[i]
        if (i, c) not in dp:
            continue
        if dp[(i, c)] > 0:
            t.append(c)
            prev_c = c

    print(r)
    print(''.join(t))

solve()
