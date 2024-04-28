def count_good_sequences():
    n, k = map(int, input().split())
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        if i % (i - 1) == 0:
            dp[i] += dp[i // (i - 1)]
        if i % (i + 1) == 0:
            dp[i] += dp[(i + 1) * (i - 1)] // (i + 1)
    return sum(dp[:k+1]) % 1000000007

print(count_good_sequences())
