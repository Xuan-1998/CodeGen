def max_points(n, seq):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if j == i - 1:
                dp[i][j] = seq[j]
            else:
                delete_points = dp[i-1][j-2] + (n-j) - i
                keep_points = dp[i-1][j]
                dp[i][j] = max(delete_points, keep_points)

    return dp[n][n]

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))
    print(max_points(n, seq))
