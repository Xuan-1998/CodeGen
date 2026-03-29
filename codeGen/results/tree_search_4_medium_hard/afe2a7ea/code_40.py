import math

n = int(input())
mod = 998244353

# Initialize dp[0][k] values
dp = [[0] * (n + 1) for _ in range(n + 1)]
for k in range(1, n + 1):
    dp[0][k] = math.comb(n, 0) * (1 / 2)**n % mod

# Calculate dp[i][j] values
for used_towers in range(1, n + 1):
    for last_signal in range(1, n + 1):
        if used_towers < n:
            # Check if it's possible to set the signal power without violating any constraints
            if (used_towers == last_signal - 1) or ((last_signal != 1) and (used_towers != last_signal - 1)):
                dp[used_towers][last_signal] = min((dp[used_towers - 1][k] for k in range(1, n + 1))) % mod
        else:
            # Handle the edge case when all towers are used or none are used
            if used_towers == n:
                dp[used_towers][last_signal] = (1 / 2)**n % mod

print(dp[n][0])  # Print the final answer
