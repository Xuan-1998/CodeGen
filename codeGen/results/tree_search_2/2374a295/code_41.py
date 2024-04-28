def find_good_sequences(n, k):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if i % j == 0:
                dp[i] += dp[j]
    return dp[n] % 10000007

n, k = map(int, input().split())
print(find_good_sequences(n, k))
