import sys

def calculate_probability(n, m, h, s):
    dp = [0] * (n + 1)
    total_players = sum(s)
    for i in range(1, n + 1):
        if i > total_players:
            return -1.0
        dp[i] = max(dp[i-1], s[h-1] / total_players) if h <= m and s[h-1] >= 1 else dp[i-1]
    return dp[-1]

n, m, h = map(int, input().split())
s = list(map(int, input().split()))
print(calculate_probability(n, m, h, s))
