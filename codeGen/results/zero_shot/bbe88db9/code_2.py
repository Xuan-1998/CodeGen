def solve():
    n = int(input())
    dp = [0] * (n + 1)
    for i in range(n, 0, -1):
        if i % 2 == 1:  # odd number of cross paintings
            dp[i] = min(dp[i], dp[i-1] + 1) if i > 1 else 1
        else:
            dp[i] = min(dp[i], dp[i+1] + 1) if i < n else 0
    return dp[1] % 1000000007

print(solve())
