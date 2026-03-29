def countGoodSubsequences():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        if a[i - 1] % i == 0:
            dp[i][0] = 1
        else:
            dp[i][0] = 0

        for j in range(1, min(i + 1, n) + 1):
            product_term = 1
            for k in range(j + 1):
                if a[i - 1] % (k + 1) == 0:
                    product_term *= 2
                else:
                    product_term *= 1
            dp[i][j] = product_term * dp[i - 1][j]

    total_good_subsequences = sum(dp[i][n] for i in range(1, n + 1))
    print(total_good_subsequences % (10 ** 9 + 7))

countGoodSubsequences()
