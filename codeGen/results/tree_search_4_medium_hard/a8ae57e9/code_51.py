from collections import defaultdict

def max_earnings(n, k, ci, pi):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    accepted_requests = []
    total_amount = 0

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            max_earn = dp[i-1][j] if j < ci[i-1] else 0
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + pi[i-1] * min(k, ci[i-1])
            if dp[i][j] > max_earn:
                accepted_requests.append((i, j))
                total_amount += pi[i-1]

    print(f"{len(accepted_requests)} {total_amount}")

    for i, j in accepted_requests:
        print(f"{i} {j}")
