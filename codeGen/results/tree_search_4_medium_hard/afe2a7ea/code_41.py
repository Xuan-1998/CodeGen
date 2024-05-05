import sys
from collections import defaultdict

mod = 998244353

n = int(sys.stdin.readline())
dp = [[0, []] for _ in range(n + 1)]
dp[0] = [1, []]

for used_towers in range(1, n + 1):
    for last_town in range(used_towers):
        if used_towers < n and last_town + 1 <= n:
            dp[used_towers].append((dp[used_towers - 1][0] * (n - used_towers) // (used_towers)) % mod)
            dp[used_towers][-1][1].extend(dp[used_towers - 1][1])
        if used_towers == n:
            dp[used_towers].append((dp[used_towers - 1][0]) % mod)

print(sum(dp[n][0]))
