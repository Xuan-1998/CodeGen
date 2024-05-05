def count_steady_tables():
    T = int(input())  # Read the number of test cases from stdin
    MOD = 10**9 + 7

    dp = [[0] * (M+1) for _ in range(N+1)]

    dp[0][j] = 1 for j in range(M+1)

    for i in range(1, N+1):
        for j in range(M+1):
            if j > 0:
                s = sum(range(j))  # Calculate the sum of the last row
                w = sum(dp[i-1][k] for k in range(s, M+1))
                dp[i][j] = (dp[i][j] + w) % MOD

    res = 0
    for j in range(M+1):
        res = (res + dp[N][j]) % MOD

    print(res)
