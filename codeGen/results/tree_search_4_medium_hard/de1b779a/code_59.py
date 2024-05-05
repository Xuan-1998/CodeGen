import sys

def maximum_profit():
    n, m, c0, d0 = map(int, input().split())
    ci = []
    di = []

    for _ in range(m):
        a, b, c, d = map(int, input().split())
        ci.append(c)
        di.append(d)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = d0

    for i in range(1, n + 1):
        dp[i][0] = c0
    for j in range(1, m + 1):
        dp[0][j] = di[j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if ci[j - 1] <= i and bi[j - 1] <= j:
                dp[i][j] = max(dp[(i - ci[j - 1])][j - 1] + di[j - 1], dp[i][j - 1])
            else:
                dp[i][j] = dp[i][j - 1]

    print(dp[n][m])

if __name__ == "__main__":
    maximum_profit()
