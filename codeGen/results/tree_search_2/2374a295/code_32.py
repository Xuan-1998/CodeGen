def is_divisible(i, j):
    return i % j == 0

def count_good_sequences(n, k):
    mod = 10**9 + 7
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j-1] + sum(is_divisible(i, p) and dp[p-1][j-1] for p in range(2, i))) % mod

    return sum(dp[n][i] for i in range(k + 1)) % mod

n, k = map(int, input().split())
print(count_good_sequences(n, k))
