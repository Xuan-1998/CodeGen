import sys

t, l, r = map(int, input().split())
mod = 10**9 + 7
ans = 0
for i in range(l, r+1):
    ans += t * (i - l) * pow(2, r - i, mod)
ans -= l * pow(2, r - l, mod)
print(ans % mod)
