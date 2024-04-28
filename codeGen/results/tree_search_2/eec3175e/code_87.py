def can_sum_subset(n, m):
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # base case: it's always possible to get a sum of 0 using no elements
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(m + 1):
            if j < m // 2:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - (m % (i + 1))] or dp[i - 1][j]

    return dp[n][m]


def main():
    n, m = map(int, input().split())
    print(can_sum_subset(n, m))


if __name__ == "__main__":
    main()
