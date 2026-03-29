def solve():
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for t in range(i, -1, -1):
            if t < k[i-1]:
                dp[i][t] = min(dp[i-1][k[i-1]-1], h[i-1] + dp[i-1][k[i-1]-h[i-1]])
            else:
                dp[i][t] = dp[i-1][t-1]

    print(dp[n][n])

if __name__ == "__main__":
    solve()
