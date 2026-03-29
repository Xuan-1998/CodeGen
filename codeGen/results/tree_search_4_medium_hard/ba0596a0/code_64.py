def can_cross(stones):
    n = len(stones)
    dp = [[False] * 3 for _ in range(n)]

    # Base cases
    dp[0][0] = True

    for i in range(1, n):
        if stones[i] - stones[i-1] <= 2:
            dp[i][stones[i] - stones[i-1]] = True

    # Fill up the table
    for i in range(n):
        for j in range(min(i+1, n), 0, -1):
            k = stones[j-1] - stones[i]
            if k >= 2 and dp[j-1][k-1]:
                dp[j][k-1] = True
            elif k == 1:
                dp[j][0] = True

    return dp[n-1][0]

# Example usage:
stones = list(map(int, input().split()))
print(can_cross(stones))
