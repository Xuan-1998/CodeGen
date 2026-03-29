def beautifulGirls(t, l, r):
    MOD = 10**9 + 7

    # Initialize dp table with infinities
    dp = [float('inf')] * (r - l + 1)
    dp[0] = 0  # base case: no groups

    for i in range(1, r - l + 1):
        for j in range(l, i + l):
            # Calculate the minimal total number of pairwise comparisons needed
            # to select the most beautiful participant from j girls
            dp[i] = min(dp[i], dp[j - l] + (j // l) * t)

    # Calculate the final result
    return sum(dp[i] * t for i in range(l, r + 1)) % MOD

t, l, r = map(int, input().split())
print(beautifulGirls(t, l, r))
