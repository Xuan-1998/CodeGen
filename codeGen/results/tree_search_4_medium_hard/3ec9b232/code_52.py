def solve():
    n = int(input())
    m = list(map(int, input().split()))

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(i + 1):
            if m[i - 1] <= i:
                dp[i][j] += dp[i - 1].min(j, m[i - 1])
            else:
                dp[i][j] += dp[i - 1][j]
    return sum(dp[-1]) % (10**9 + 7)

print(solve())
