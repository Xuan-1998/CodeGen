def count_good_sequences():
    n, k = map(int, input().split())
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for j in range(2, n + 1):
        for i in range(j, n + 1):
            if i % j == 0:
                if j == 1 or i // j > 0:
                    dp[i][j] = sum(dp[k][j] for k in range(1, i // j)) + (i == 1)
                else:
                    dp[i][j] = 1
            else:
                dp[i][j] = 0

    return sum(dp[n][i] for i in range(k + 1)) % 1000000007

print(count_good_sequences())
