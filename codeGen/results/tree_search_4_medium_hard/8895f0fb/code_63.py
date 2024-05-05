from collections import defaultdict

def expected_carries(N):
    memo = defaultdict(int)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(i + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = min(j, N - j)
                for k in range(j):
                    dp[i][j] += (memo[(k, N - i - 1)] or 0)

    total_pairs = sum(range(N + 1))
    expected_carries = sum(dp[N][i] * (N - i) for i in range(N + 1)) / total_pairs

    return float(expected_carries)
