import sys

# Read input from stdin
n = int(input())
marks_above_water = list(map(int, input().split()))

# Initialize memoization dictionary and dp array
memo = {}
dp = [0] * (n + 1)

for i in range(1, n + 1):
    # Calculate minimum sum of marks below water level for day i
    min_sum = float('inf')
    for j in range(i):
        if j not in memo:
            memo[j] = dp[j]
        prev_marks_above_water = marks_above_water[j]
        min_sum = min(min_sum, dp[j] + (i - 1) - prev_marks_above_water)
    dp[i] = min_sum

# Print minimum possible sum of marks below water level
print(dp[-1])
