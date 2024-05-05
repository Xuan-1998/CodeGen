===BEGIN PLAN===
dp = [1] * len(array)   # Initialize a dynamic programming table with ones

for i in range(1, len(array)):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_length = max(dp)
count = sum(1 for x in dp if x == max_length)
===END PLAN===
