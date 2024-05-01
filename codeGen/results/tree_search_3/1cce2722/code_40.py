def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[0] * (105 + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        aj = a[i - 1]
        for k in range(aj + 1, 106):
            dp[i][k] = max(dp[i-1][k], dp[i-1][min(k-1, aj)] + (1 if aj == k+1 else 0))

    return max(dp[n])

print(solve())
