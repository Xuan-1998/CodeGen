import sys
t, l, r = map(int, input().split())
f = lambda n: min(n.bit_length(), (n - 1).bit_length() + 1)
result = sum(t[i]*f(l+i) for i in range(r-l+1)) - l*f(r)
print(result % (10**9 + 7))
