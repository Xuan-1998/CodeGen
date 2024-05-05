def solve():
    n, q = map(int, input().split())
    signs = list(input())

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = 0
        for j in range(i - 1, -1, -1):
            if signs[j] == signs[i]:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i-1][i])
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][i])

    for _ in range(q):
        l, r = map(int, input().split())
        print(min(r - l + 1, dp[r][r] - dp[l-1][l-1]))

if __name__ == "__main__":
    solve()
