# Define the number of rooms and the portal array
n = int(input())
p = list(map(int, input().split()))

# Initialize the DP table with infinity values
dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]

# Base case: reaching room n+1 requires no more moves
dp[n][n] = 0

# Fill up the DP table using a bottom-up approach
for i in range(n - 1, -1, -1):
    for k in range(i + 1):
        # If we're in room i and have reached p_i
        if k == p[i]:
            # Calculate the minimum number of moves based on the ceiling crosses
            dp[i][k] = min(dp[i][k], dp[p[i]][p[i]] + (dp[i][k] % 2))
        else:
            # If we haven't reached p_i yet, calculate the minimum number of moves to reach it and add 1 for the extra move
            dp[i][k] = min(dp[i][k], dp[p[i]][p[i]] + 1)

# The answer is the minimum number of portal moves needed to reach room n+1 from room 1
print(min(dp[0]))
