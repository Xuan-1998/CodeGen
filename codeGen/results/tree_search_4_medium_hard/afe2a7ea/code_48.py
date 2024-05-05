def solve():
    n = int(input())
    MOD = 998244353
    dp = [[0]*(n+1) for _ in range(n+1)]

    # Base case: dp[0][k] = 1 for all k (no towers)
    for k in range(n+1):
        dp[0][k] = 1

    # Fill up the DP table
    for i in range(1, n+1):
        for k in range(min(i+1, n+1)):
            if i == 1:
                dp[i][k] = 1
            else:
                dp[i][k] = (dp[i-1][k-1] + sum(dp[j-1][k-1] for j in range(2, i+1))) % MOD

    # Calculate the probability
    prob = 0
    for k in range(1, n+1):
        prob += dp[n][k]
    print(prob % MOD)

solve()
