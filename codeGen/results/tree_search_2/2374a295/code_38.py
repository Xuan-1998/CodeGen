def count_good_sequences(n, k):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            if j % i == 0:
                dp[i] += dp[j]
    return sum(dp[:k+1]) % 1000000007

n, k = map(int, input().split())
print(count_good_sequences(n, k))
