def max_profit(n, m, c0, d0):
    # Initialize dp table with -float('inf') values
    dp = [[float('-inf')] * (n+1) for _ in range(m)]

    # Base case: no dough and no stuffings
    dp[-1][-1] = 0

    for i in range(m):
        for j in range(n+1):
            if j < c0:
                dp[i][j] = max(dp[max(i-1, 0)][j], d0)
            else:
                dp[i][j] = max(dp[max(i-1, 0)][j-ci[i]] + di[i], dp[i][j])

    return dp[m-1][n]

# Example input
n, m, c0, d0 = map(int, input().split())
ai, bi, ci, di = [], [], [], []
for _ in range(m):
    a, b, c, d = map(int, input().split())
    ai.append(a)
    bi.append(b)
    ci.append(c)
    di.append(d)

# Compute the maximum profit
max_profit_val = max_profit(n, m, c0, d0)
print(max_profit_val)
