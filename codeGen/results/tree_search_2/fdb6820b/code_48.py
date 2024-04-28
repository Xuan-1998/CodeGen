def count_ways(A, N):
    MOD = 10**9 + 7

    # Create a memoization table dp with size N+1
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: there is one way to reach a sum of 0

    for i in range(1, N + 1):
        for num in A:
            if i >= num:
                dp[i] += dp[i - num]
            dp[i] %= MOD

    return dp[N]

m, N = map(int, input().split())
A = list(map(int, input().split()))
print(count_ways(A, N))
