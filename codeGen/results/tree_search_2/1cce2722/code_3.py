def max_points(n):
    dp = [0] * (n + 1)
    for s in range(2, n + 1):
        if s % 2 == 0:  # Even number of elements
            dp[s] = dp[s - 1]
        else:
            dp[s] = max(dp[s - 2] + s, dp[s - 1] + 1)
    return dp[n]

if __name__ == "__main__":
    n = int(input())
    print(max_points(n))
