def subsetSumDivisible(n, m):
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Base case: A set with no elements has sum 0, which is a multiple of any number
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = True
            elif j < m and (dp[i-1][j] or (i % m == 0 and j != 0)):
                dp[i][j] = True

    return int(any(dp[n][i] for i in range(m + 1)))

# Test the function with some sample inputs
n, m = map(int, input().split())
print(subsetSumDivisible(n, m))
