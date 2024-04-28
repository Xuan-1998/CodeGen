import sys

def solve(n, m, arr):
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        if i == 0:
            continue
        j = 0
        while j <= m:
            if arr[i - 1] % m <= j:
                dp[i][j] = True
            else:
                break
            j += 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            k = (j - arr[i - 1]) % m
            if k < 0:
                k += m
            if dp[i - 1][k]:
                dp[i][j] = True

    print(1 if dp[n][m - 1] else 0)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
solve(n, m, arr)
