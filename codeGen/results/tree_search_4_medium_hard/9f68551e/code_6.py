import sys

def min_mana(n, k, h):
    max_k = max(k)
    dp = [[0] * (max_k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(max_k + 1):
            if j < h[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][k] + (k - h[i - 1]) % 2 for k in range(h[i - 1], j + 1))

    return min(dp[n])

t = int(input())
for _ in range(t):
    n = int(input())
    k = list(map(int, input().split()))
    h = list(map(int, input().split()))
    print(min_mana(n, k, h))
