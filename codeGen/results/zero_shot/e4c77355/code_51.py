# Read the input array
input_array = list(map(int, input().split()))

# Initialize a dynamic programming table to store the length of the longest increasing subsequence ending at each element
dp = [1] * len(input_array)

# Initialize the maximum length of the longest increasing subsequence
max_length = 1

# Iterate through the array
for i in range(1, len(input_array)):
    for j in range(i):
        # Check if the current element is greater than the previous element
        if input_array[i] > input_array[j]:
            # Update the length of the longest increasing subsequence ending at the current element
            dp[i] = max(dp[i], dp[j] + 1)
    # Update the maximum length of the longest increasing subsequence
    max_length = max(max_length, dp[i])

# Print the result
print(max_length)
