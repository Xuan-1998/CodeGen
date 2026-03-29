import sys

def min_operations():
    n = int(input())
    a = list(map(int, input().split()))
    max_val = max(a)
    dp = [[0] * (max_val + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, a[i - 1]):
            if a[i - 1] > j:
                dp[i][j] = 0
            else:
                min_ops = float('inf')
                for k in range(i):
                    if a[k] <= j:
                        min_ops = min(min_ops, dp[k][a[k]])
                dp[i][j] = min_ops + (j - a[i - 1])

    return max(j for i in range(n) for j in range(1, a[i] + 1) if dp[i + 1][j])

print(min_operations())
