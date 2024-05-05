import sys
t, l, r = map(int, input().split())
print((t * (f(l) + f(l+1) + ... + f(r))) % (10**9 + 7))
