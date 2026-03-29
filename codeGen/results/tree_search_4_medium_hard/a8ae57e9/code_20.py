def solve():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    p = []
    for _ in range(n):
        g, t = map(int, input().split())
        p.append((g, t))

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    d = {}

    for i in range(1, n + 1):
        for j in range(k + 1):
            if i <= c[j]:
                dp[i][j] = max(dp[i-1][j], p[i-1][1] * c[j])
                d[(i, j)] = j
            else:
                dp[i][j] = dp[i-1][j]

    accepted_requests = 0
    total_money_earned = dp[n][k]
    for i in range(n, 0, -1):
        if dp[i][d[(i, d[(i, k)])]] == p[i-1][1] * c[d[(i, k)]]:
            accepted_requests += 1
            total_money_earned -= p[i-1][1]
            print(f"{i} {d[(i, k)]}")

    print(accepted_requests)
    print(total_money_earned)

if __name__ == "__main__":
    solve()
