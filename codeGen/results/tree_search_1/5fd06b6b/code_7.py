n = int(input().strip())
marks_above = list(map(int, input().split()))

# Initialize dp array with infinity
dp = [float('inf')] * (n + 1)
dp[0] = 0  # No marks below water level before the first day

# Calculate the minimum number of marks below the water level for each day
for i in range(1, n + 1):
    dp[i] = min(dp[i], dp[i-1] + (i - 1 - marks_above[i-1]))

# The result is the minimum number of marks below the water level after n days
print(dp[n])
