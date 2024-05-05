import sys

n = int(input())  # Read the number of trips from stdin
dp = [0] * (n + 1)  # Initialize dp array with zeros

for i in range(1, n + 1):
    # Calculate the minimum cost for trip i
    dp[i] = min(dp[i-1] + 20,
                 dp[max(0, i-90)] + 50,
                 dp[max(0, i-14*60)] + 120)

# Print the minimum cost for each trip
for i in range(1, n + 1):
    print(dp[i])
