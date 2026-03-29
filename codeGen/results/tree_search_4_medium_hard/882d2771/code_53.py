=code block=
import sys
input = sys.stdin.read().split()
t, l, r = map(int, input)
mod = 10**9 + 7

dp = [0] * (r - l + 1)

def f(n):
    if n == 2:
        return 3
    if n % 2 == 0:
        return 2 * f(n // 2) + 1
    return f((n + 2) // 3) + (n + 2) // 3 - n + 1

for i in range(l, r + 1):
    if i % 2 == 0:
        dp[i - l] = 2 * dp[(i - l) // 2] + 1
    else:
        dp[i - l] = f((i - l + 2) // 3) + (i - l + 2) // 3 - i + l

ans = sum(t * dp[i] for i in range(l, r + 1)) - l * f(r)
print(ans % mod)
=code block=
