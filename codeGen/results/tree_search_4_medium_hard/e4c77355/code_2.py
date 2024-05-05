===BEGIN CODE===
# Read the input array from stdin
arr = [int(i) for i in input().split()]

# Initialize a dictionary to store the dynamic programming values
dp = {i: 1 for i in range(len(arr))}

# Initialize the maximum length of increasing subsequence
max_length = 1

for i in range(1, len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp.get(i, 0), dp.get(j, 0) + 1)
    max_length = max(max_length, dp[i])

# Print the length of the longest increasing subsequence to stdout
print(max_length)

===END CODE===
