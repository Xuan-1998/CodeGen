import sys

dp = [[0] * (1 << k) for k in range(k + 1)]
for i in range(1, k + 1):
    dp[i][0] = 1
    for j in range(1, 2 ** i - 1):
        if i == k:
            dp[i][j] = 1 if j >= (1 << (k - 1)) - 1 else 0
        else:
            dp[i][j] = 0
            if not (j & (1 << i)):
                dp[i][j] += dp[i - 1][j]
            if j & (1 << i):
                for k in range(2 ** (i - 1) - 1, 2 ** i - 1):
                    dp[i][j] += dp[i - 1][k]

n = int(input())
for _ in range(n):
    n, k = map(int, input().split())
    xor_result = 0
    and_result = (1 << k) - 1
    for _ in range(n):
        x = int(input())
        xor_result ^= x
        and_result &= x
    print(dp[k][and_result] % (10 ** 9 + 7))
