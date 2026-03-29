def can_cross(stones):
    n = len(stones)
    dp = [[False] * (n+1) for _ in range(n+1)]

    for i in range(n-1, -1, -1):
        for j in range(i+1, n+1):
            if j > stones[-1]:
                break
            for k in range(i+1, min(j+1, stones[-1]+1)):
                if abs(j-(i+k)) <= k:
                    dp[i][j] = dp[i][k]
                    break
            for k in range(max(0, j-2), i):
                if abs(j-k) in (1, 2):
                    dp[i][j] = True
                    break

    return dp[0][stones[-1]]

# Example usage:
stones = [0, 5, 3, 6, 1, 7]
print(can_cross(stones))  # Output: True
