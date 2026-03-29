# Step 1: Define the input
input_array = list(map(int, input().split()))

# Step 2: Create a dynamic programming table
dp = [1] * len(input_array)

# Step 3: Iterate through the array and update dp values
for i in range(len(input_array)):
    for j in range(i):
        if input_array[i] > input_array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# Step 4: Find the maximum length of increasing subsequence
max_length = max(dp)

print(max_length)
