# Read input array from stdin
input_array = [int(x) for x in input().split()]

# Initialize DP array with all elements set to 1
dp = [1] * len(input_array)

# Iterate through the array, updating DP values based on previous longest increasing subsequence and current element
for i in range(1, len(input_array)):
    for j in range(i):
        if input_array[i] > input_array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# The length of the longest increasing subsequence is the maximum value in the DP array
print(max(dp))
