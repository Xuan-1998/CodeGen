def solve():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        c, p = map(int, input().split())
        for j in range(1, min(i, k) + 1):
            dp[i][j] = max(dp[i-1][min(j, k - 1)] + p, dp[i-1][j])

    accepted_requests = []
    total_money_earned = dp[n][k]
    tables_used = 0

    for i in range(n, 0, -1):
        if dp[i][tables_used] != dp[i-1][tables_used]:
            accepted_requests.append((i, p))
            total_money_earned -= p
            tables_used += 1

    print(total_money_earned)
    print(len(accepted_requests))

    for request in accepted_requests:
        table = min(request[0], k - 1)
        print(*request, table)

if __name__ == "__main__":
    solve()
