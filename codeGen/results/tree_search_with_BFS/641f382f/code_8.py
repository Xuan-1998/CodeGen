from math import gcd
from sys import stdin, stdout

def min_operations(n, arr):
    dp = [[float('inf')] * n for _ in range(n)]
    cnt = arr.count(1)
    if cnt > 0:
        return n - cnt

    for i in range(n):
        g = arr[i]
        for j in range(i, n):
            g = gcd(g, arr[j])
            if g == 1:
                dp[i][j] = j - i

    for k in range(n):
        for i in range(n - k):
            j = i + k
            if i > 0:
                dp[i - 1][j] = min(dp[i - 1][j], dp[i][j] + 1)
            if j < n - 1:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

    return min(dp[i][j] for i in range(n) for j in range(i, n)) + 1 if dp[0][n - 1] < float('inf') else -1

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
stdout.write(str(min_operations(n, arr)))

