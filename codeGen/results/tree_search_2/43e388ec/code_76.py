import sys
from functools import reduce

def left_shift(b, i):
    return b << i

d = {}
a = int(input(), 2)
b = int(input(), 2)

for i in range(315):
    d[i] = (a ^ left_shift(b, i)) % (10**9 + 7)

print(reduce(lambda x, y: x + y, map(d.get, range(315))) % (10**9 + 7))
