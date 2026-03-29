import sys

def f(n):
    return n.bit_length()

t, l, r = map(int, input().split())
result = sum(ti * fi for ti, fi in zip(map(int, [0] * (l - 1) + list(range(l, r + 1))), map(f, range(l, r + 1)))) % (10**9 + 7)
print(result)
