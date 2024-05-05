import sys

# Initialize memoization array dp with size C+1 by N+M
dp = [[0] * (N + M) for _ in range(C + 1)]
dp[0][j] = 1 for j in range(N + M)

for r in range(1, C + 1):
    for j in range(min(N, M)):
        # Transition relationship: either add a new sphere with its radius
        dp[r][j] += (j > 0) * dp[r - 1][j - 1]
        
        # or reuse an existing sphere with a smaller radius
        for i in range(j):
            if r <= U[i]:
                dp[r][j] = (dp[r][j] + dp[U[i]][j - 1]) % (10**9 + 7)
            if r <= L[i]:
                dp[L[i]][j] = (dp[L[i]][j] + dp[r][j - 1]) % (10**9 + 7)

for j in range(N + M):
    print(dp[C][j], end=' ')
print()
