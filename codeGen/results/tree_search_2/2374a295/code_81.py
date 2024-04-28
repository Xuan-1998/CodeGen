def good_sequences(n, k):
    dp = [1] + [0] * n
    for i in range(2, n+1):
        for j in range(1, i//j+1):
            if i % j == 0:
                dp[i] += dp[i//j]
    return sum(dp) % 1000000007

n, k = map(int, input().split())
print(good_sequences(n, k))
