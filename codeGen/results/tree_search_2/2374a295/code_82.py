def find_good_sequences(n, k):
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(1, i // j + 1):
            if i % j == 0:
                dp[i] += dp[j]
        dp[i] %= 1000000007

    return dp[n]

n, k = map(int, input().split())
print(find_good_sequences(n, k))
