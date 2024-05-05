def solve(n, m):
    MOD = 10**9 + 7

    # Initialize dp array with zeros
    dp = [0] * (n + 1)

    # Base case: only one way to create an empty array
    dp[0] = 1

    for i in range(1, n + 1):
        # For each number m_i in M
        for j in range(n, m[i - 1] - 1, -1):
            # If the current number is not present in the previous arrays
            if dp[j - m[i - 1]]:
                # Add the number of ways to create the previous arrays
                dp[j] += dp[j - m[i - 1]]
        # Take modulo at each step to avoid overflow
        dp[i] %= MOD

    return dp[n]

n = int(input())
m = list(map(int, input().split()))
print(solve(n, m))
