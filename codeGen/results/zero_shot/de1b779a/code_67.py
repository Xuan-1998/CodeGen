def max_profit(n, m, c0, d0, ai, bi, ci, di):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(m + 1):
        dp[0][i] = d0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if ai[j - 1] >= bi and c0 >= ci:
                dp[i][j] = max(dp[i - 1][j], di + dp[i - 1][j - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]

# Example input (you can modify this)
n = int(input())
m = int(input())
c0, d0 = map(int, input().split())
ai = [int() for _ in range(m)]
bi = [int() for _ in range(m)]
ci = [int() for _ in range(m)]
di = [int() for _ in range(m)]

for i in range(m):
    ai[i], bi[i], ci[i], di[i] = map(int, input().split())

# Call the max_profit function with the example input
max_tugriks = max_profit(n, m, c0, d0, ai, bi, ci, di)
print(max_tugriks)
