import sys

t, l, r = map(int, input().split())
mod = int(1e9 + 7)

dp = [0] * (r + 1)
for i in range(2, r + 1):
    if i % 2 == 0:
        dp[i] = min(dp[i // 2], dp[i // 4] if i % 4 == 0 else dp[(i + 3) // 4])
    else:
        dp[i] = min(dp[i - 1], dp[(i + 1) // 2])

result = sum(t * (r - i) for i in range(l, r + 1)) % mod
print(result)
