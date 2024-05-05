===BEGIN CODE===
import sys

n = int(input())  # Number of trips
dp = [0] * (10**9 + 1)  # Initialize DP table with all zeros

for _ in range(n):
    t = int(input())  # Time of the current trip
    for i in range(t, -1, -1):  # Iterate from the current time to the start of the system
        dp[t] = min(dp[t], 50 + dp[max(0, i - 89)])  # 90-minute ticket
        dp[t] = min(dp[t], 120 + dp[max(0, i - 1439)])  # Day-long ticket
    print(dp[t])  # Print the minimum cost for the current trip

===END CODE===
