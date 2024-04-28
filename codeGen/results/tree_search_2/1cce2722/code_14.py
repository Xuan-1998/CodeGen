def maximum_points(n, a):
    dp = [[0, 0] for _ in range(n + 1)]

    for i in range(2, n + 1):
        if a[i-1] == a[i-2]:
            dp[i][1] = max(dp[i-1][0], dp[i-2][1])
        else:
            dp[i][1] = dp[i-1][1]

    return dp[n][1]

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(maximum_points(n, a))
