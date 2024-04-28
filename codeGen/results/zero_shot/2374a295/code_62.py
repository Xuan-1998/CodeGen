n, k = map(int, input().split())
print(count_good_sequences(n, k) % 10000007)

def count_good_sequences(n, k):
    dp = [0] * (k + 1)
    dp[0] = n
    for i in range(1, k + 1):
        dp[i] = sum(dp[j] // (j + 1) for j in range(i))
    return dp[-1]
