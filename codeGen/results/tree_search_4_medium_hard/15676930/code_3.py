from collections import defaultdict

def max_hare_joy(n):
    a, b, c = [int(x) for x in input().split()], [int(x) for x in input().split()], [int(x) for x in input().split()]

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    memo = defaultdict(int)

    def solve(i, j):
        if i < 0 or j < 0:
            return 0
        if i == 0 and j == 0:
            return 0

        if (i, j) not in memo:
            dp[i][j] = max(solve(i - 1, j - 1) + c[i], solve(i - 1, 0) + b[i])
            memo[(i, j)] = dp[i][j]

        return dp[i][j]

    return solve(n, n)
