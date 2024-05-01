from collections import defaultdict

def max_points(n, sequence):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    memo = defaultdict(int)

    for i in range(1, n):
        for j in range(1, n - 1):
            if sequence[i] == sequence[j - 1] + 1 or sequence[i] == sequence[j + 1] - 1:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]

n = int(input())
sequence = [int(x) for x in input().split()]

print(max_points(n, sequence))
