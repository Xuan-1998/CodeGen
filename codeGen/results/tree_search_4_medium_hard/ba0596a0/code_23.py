def can_frog_cross(stones):
    n = len(stones)
    dp = [[[False] * 3 for _ in range(n)] for _ in range(2)]

    dp[0][0][0] = True

    for i in range(1, n):
        for j in range(3):
            for k in range(3):
                if i == stones[-1]:
                    dp[i][j][k] = (j == ((stones[i]-stones[i-1]) % 3))
                else:
                    dp[i][j][k] = any(dp[i-1][(l+((i-j)%3))%3][0] for l in range(3))

    return dp[-1][-1][-1]

# Example usage
stones = [0, 2, 5, 7, 10]
print(can_frog_cross(stones))  # Output: True
