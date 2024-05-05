from sys import stdin

def hares_joys():
    n = int(stdin.readline())
    a = [int(x) for x in stdin.readline().split()]
    b = [int(x) for x in stdin.readline().split()]
    c = [int(x) for x in stdin.readline().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize base cases
    for j in range(n + 1):
        dp[1][j] = c[0]

    for i in range(2, n + 1):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = a[i - 1] + dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][k] + (a[i - 1] if k == 0 else b[i - 1]) for k in range(j))

    return dp[n][n]

print(hares_joys())
