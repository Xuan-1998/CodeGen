def smallest_string(n, k):
    if k > n:
        return ""

    s = input().strip()
    dp = [[[] for _ in range(k + 1)] for _ in range(n + 1)]

    memo = {}

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if s[i - 1] <= s[j - 1]:
                dp[i][j] = [s[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j - 1]

    return "".join(dp[n][k])

n, k = map(int, input().split())
print(smallest_string(n, k))
