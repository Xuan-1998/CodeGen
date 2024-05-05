def max_earnings(n, k, requests):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if not requests[i - 1][1]:  # group size too large
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                ci, pi = requests[i - 1]
                if j >= ci:  # table has enough capacity
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + pi)
                else:
                    dp[i][j] = dp[i - 1][j]

    total_earnings = dp[n][k]
    accepted_requests = 0
    for i in range(n, 0, -1):
        if requests[i - 1][1]:  # group size acceptable
            ci, pi = requests[i - 1]
            j = min(k, ci)
            total_earnings -= pi
            k -= j
            accepted_requests += 1

    print(f"{accepted_requests} {total_earnings}")
