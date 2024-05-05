def solve(n, k, requests):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        ci, pi = requests[i - 1]
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = max(dp[i - 1][j], pi)
            else:
                accept = dp[i - 1][j - 1] + ci * pi
                decline = dp[i - 1][j]
                dp[i][j] = max(accept, decline)

    accepted_requests = []
    total_amount = 0
    j = k
    for i in range(n, -1, -1):
        if dp[i][j] > dp[i - 1][j]:
            ci, pi = requests[i - 1]
            accepted_requests.append((i, j))
            total_amount += pi
            j -= ci
        else:
            j -= 1

    print(f"{len(accepted_requests)} {total_amount}")
    for request in accepted_requests:
        print(*request)

n, k = map(int, input().split())
requests = [list(map(int, input().split())) for _ in range(n)]
solve(n, k, requests)
