def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == j:
                dp[i][j] = 1
            else:
                min_squares = float('inf')
                for k in range(max(0, i - j), min(i, j) + 1):
                    min_squares = min(min_squares, dp[k][j - k] + dp[i - k][k])
                dp[i][j] = min_squares + 1

    return dp[n][m]

def main():
    n, m = map(int, input().split())
    print(min_squares(n, m))

if __name__ == "__main__":
    main()
