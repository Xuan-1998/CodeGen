def solve():
    a, b = map(int, input().split())
    dp = [[0] * (b+1) for _ in range(a+1)]

    for i in range(1, a+1):
        for j in range(b+1):
            if i == 1:
                dp[i][j] = ((a & 1) ^ (b >> j)) % (10**9 + 7)
            else:
                dp[i][j] = (dp[i-1][j] + ((a & 1) ^ (b >> j)) % (10**9 + 7))

    print(sum(dp[a]) % (10**9 + 7))
