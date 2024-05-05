===BEGIN CODE===
def solve(n, t):
    dp = [0] * (n + 1)
    fractional_part = [int(x) for x in input().split(".")[1]]

    for i in range(1, n + 1):
        if t >= 1:  # time constraint
            dp[i] = max(dp[i-1], round(fractional_part[i-1]) / (10 ** (i - 1)))
        else:
            dp[i] = dp[i-1]
        t -= 1

    return int(dp[n])

n, t = map(int, input().split())
print(solve(n, t))
===END CODE===
