def min_sum_below_water(n, marks):
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        for k in range(i):
            if k == 0:
                dp[i][k] = dp[i-1][k]
            else:
                dp[i][k] = min(dp[j][m-j-1] + (i-j-1)*m for j in range(k) for m in range(k+1))

    return dp[n][n]

if __name__ == "__main__":
    n = int(input())
    marks = list(map(int, input().split()))
    print(min_sum_below_water(n, marks))
