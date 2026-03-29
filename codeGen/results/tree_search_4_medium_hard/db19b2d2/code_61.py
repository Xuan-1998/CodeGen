from math import prod

def solve(n, m, h, s):
    dp = [[[0 for _ in range(m+1)] for _ in range(m+1)] for _ in range(n+1)]

    # Base case: If the total number of players from all departments is less than n,
    # then it's impossible to form a team with at least one player from the department of interest.
    for j in range(m+1):
        dp[0][j][h] = 1

    for i in range(1, n+1):
        for j in range(1, min(i+1, m+1)+1):
            for k in range(j-1, min(j+h, m)+1):
                if k == h:
                    dp[i][j][k] = (s[h-1] / sum(s)) * (dp[i-1][j-1][k-1] + dp[i][j-1][k])
                else:
                    dp[i][j][k] = dp[i-1][j][k]
            if j > 0:
                dp[i][j][j] = 1

    return prod(dp[n][i][h] for i in range(m+1)) / (prod(s) ** n)
