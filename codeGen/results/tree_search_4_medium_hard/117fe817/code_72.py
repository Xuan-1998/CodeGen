import math

def find_digit_one(n):
    MOD = 10**9 + 7
    dp = [[0] * (math.ceil(math.log2(n)) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(int(math.log2(i)), -1, -1):
            if i >= 10**(j+1):
                dp[i][j] = (dp[i // 10**j][j] + min(j, 1)) % MOD
            else:
                dp[i][j] = 0

    return sum(dp[n][i] for i in range(math.ceil(math.log2(n)) + 1))
