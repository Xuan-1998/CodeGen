import sys

n = int(input())  # read number of trips from stdin

# initialize DP array with infinity values
dp = [float('inf')] * (n + 1)

dp[0] = 0  # base case: no cost to activate after the first trip

for i in range(1, n + 1):
    if i < 90:
        dp[i] = dp[i-1] + 20
    elif i < 1440:
        dp[i] = min(dp[i-1] + 50, dp[i-2] + 50)
    else:
        dp[i] = min(dp[i-1] + 120, dp[i-2] + 120)

# print the minimum cost to activate tickets after each trip
for i in range(n):
    print(int(dp[i+1]))
