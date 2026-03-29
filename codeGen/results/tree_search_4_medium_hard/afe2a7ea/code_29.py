def solve():
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(n + 2)]
    
    # Base case: when all towers are unused, the probability is 2^(-n)
    for i in range(1, n + 1):
        dp[i][0] = 2 ** (-i)
    
    # State transition relationship
    for i in range(1, n + 2):
        for j in range(1, min(i, n) + 1):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 998244353
    
    # Final answer: sum of probabilities over all states where there's only one unused tower left
    return sum(dp[n][i] for i in range(1, n + 1)) % 998244353

print(solve())
