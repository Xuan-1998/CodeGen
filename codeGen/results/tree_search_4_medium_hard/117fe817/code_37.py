def count_ones(n):
    MOD = 10**9 + 7
    dp = [[0] * (n + 1) for _ in range(31)]

    for k in range(30, -1, -1):
        if k == 29:
            for i in range(n // 10**k, -1, -1):
                dp[k][i] += (str(i)[k:] or '0').count('1')
        else:
            for i in range(n // 10**k + 1):
                if i >= 10**(k+1):
                    count = sum(dp[k-1][j] for j in range(10))
                else:
                    count = dp[k-1][i] + (str(i)[k] == '1')
                dp[k][i] += count

    return sum(dp[0])

n = int(input())
print(count_ones(n) % MOD)
