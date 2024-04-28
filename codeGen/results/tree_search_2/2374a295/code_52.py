def count_good_sequences(n, k):
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        if i % (i - 1) == 0:  # i is divisible by i-1
            dp[i] = dp[i - 1]
        else:
            dp[i] = 0
            
    return sum(dp[:k]) % 1000000007

n, k = map(int, input().split())
print(count_good_sequences(n, k))
