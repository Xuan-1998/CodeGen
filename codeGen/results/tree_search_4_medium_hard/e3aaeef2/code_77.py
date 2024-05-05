def solve():
    t = int(input())
    memo = {}

    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i > 0 and j > 0:
                    if j % 10 != 0:
                        dp[i][j] = min(dp[i - 1][k] for k in range(j)) + 1
                    else:
                        dp[i][j] = dp[i - 1][j]
                elif i == 0:
                    dp[i][j] = j

        print((dp[m][n]) % (10**9 + 7))

if __name__ == "__main__":
    solve()
