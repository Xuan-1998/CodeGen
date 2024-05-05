# Initialize dp array with zeros
dp = [[[0.0 for _ in range(h+1)] for _ in range(n+1)] for _ in range(m+1)]

# Base case: If we have already selected n players, the probability is 1 if h departments are seen and 0 otherwise.
for i in range(m+1):
    dp[i][n][i] = 1.0

# Transition relationship: Calculate the probability that a randomly formed team will have at least one player from the department of interest given that we have already selected i players and seen j departments.
for i in reversed(range(n+1)):
    for j in range(m):
        if j < h:
            dp[j][i][j] = 0.5 * (dp[j][i-1][j] + dp[j][i-1][j+1])
        else:
            dp[j][i][j] = dp[j][i-1][j]

# Calculate the final probability
prob = 0.0
for i in range(m):
    prob += dp[i][n][h]
print(prob)
