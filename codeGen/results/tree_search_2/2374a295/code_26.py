def good_sequences(n, k):
    dp = [[0] * (n+1) for _ in range(k+1)]
    
    dp[0][n] = 1
    
    for i in range(1, n+1):
        for j in range(min(i, k), -1, -1):
            if j < k:
                dp[j][i] += dp[j-1][i//j]
    
    print((dp[k][n] + 998244353) % (2**31 - 1))

# Receive inputs from stdin
n, k = map(int, input().split())

# Call the function and print the result
good_sequences(n, k)
