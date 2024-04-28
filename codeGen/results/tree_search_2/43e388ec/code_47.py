code block
from collections import defaultdict

dp = defaultdict(int)
dp[0] = 0

for a in range(1, 2**19):
    for b in range(a+1):
        dp[(a, b)] = (dp[(a-1, b<<1)] + dp[(a, b-1)]) % int(10**9+7)

print(sum(dp.values()) % int(10**9+7))
