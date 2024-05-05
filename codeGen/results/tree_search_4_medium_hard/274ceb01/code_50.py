def min_marks_below_water(n, marks):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            for k in range(j, -1, -1):
                if k > j:
                    break
                dp[i][j] = min(dp[i][j], dp[k-1][k-j] + (i-k)*j)

    return dp[n][n]

if __name__ == "__main__":
    n = int(input())
    marks = list(map(int, input().split()))
    print(min_marks_below_water(n, marks))
