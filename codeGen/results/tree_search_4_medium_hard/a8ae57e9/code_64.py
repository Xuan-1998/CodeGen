def solve(requests):
    n, k = len(requests), sum(request[0] for request in requests)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = max(dp[i - 1][j], requests[i - 1][1] * min(k, requests[i - 1][0]))

    accepted_requests = 0
    total_earned = 0
    for i in range(n, 0, -1):
        if dp[i][k] > dp[i - 1][k]:
            accepted_requests += 1
            total_earned += requests[i - 1][1]
            k -= requests[i - 1][0]

    print(accepted_requests, total_earned)

    for i in range(n - 1, -1, -1):
        if dp[i][k] > dp[i - 1][k]:
            print(i + 1, k)
            accepted_requests -= 1
            k += requests[i][0]
