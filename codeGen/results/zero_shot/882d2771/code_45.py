import sys
t, l, r = map(int, input().split())
print((0*t*f(l)) + (1*t*f(l+1)) + ... + (r*t*f(r)) - l*f(r) % (10**9+7))
