dp = [[False for _ in range(2)] for _ in range(n+1)]

for k in range(1, n+1):
    for prev_mood in range(2):
        if (k % 2) == 0:  # If we're at an even-numbered vertex
            dp[k][prev_mood] = not dp[k-1][prev_mood]
        else:
            dp[k][prev_mood] = dp[k-1][not prev_mood]

print("YES" if (n % 2) == 0 or dp[n][0] or dp[n][1] else "NO")
