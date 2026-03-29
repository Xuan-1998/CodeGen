import sys

def f(n):
    if n == 2:
        return 3
    else:
        return f(n-1) + n-1

t, l, r = map(int, input().split())
mod = 10**9 + 7

ans = 0
for i in range(l, r+1):
    ans += t[i-l] * f(i) - l * f(r)
    ans %= mod

print(ans)
