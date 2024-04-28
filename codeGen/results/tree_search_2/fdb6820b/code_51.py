def count_ways(A, N):
    MOD = 10**9 + 7
    n = len(A)
    dp = [0] * (N+1)
    dp[0] = 1

    for i in range(1, N+1):
        for x in A:
            if i >= x:
                dp[i] += dp[i-x]
                dp[i] %= MOD

    return dp[N]

# Example usage
A = [1, 2, 3]
N = 4
print(count_ways(A, N))  # Output: 7 (mod 10^9 + 7)
