import sys
from math import comb

def solve():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))

    if sum(s) < n:
        print(-1)
        return

    prob = 0.0
    for k in range(n):
        for i in range(m):
            if i == h - 1:
                prob += comb(s[i], k + 1) / (comb(sum(s), k + 1) or sys.float_info.epsilon)

    print(prob)
