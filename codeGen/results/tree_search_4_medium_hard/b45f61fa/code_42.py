import sys

def min_multiplications(p):
    n = len(p)
    dp = [[float('inf')] * (n - 1) for _ in range(n)]

    for i in range(n - 1):
        dp[i][i] = 0

    for chain_len in range(2, n + 1):
        for start in range(n - chain_len + 1):
            end = start + chain_len - 1
            for split_at in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][split_at] + p[start]*p[split_at+1]*p[end])

    return dp[0][-1]

n = int(input())
p = [int(x) for x in input().split()]
print(min_multiplications(p))
